# -*- coding: utf-8 -*-
import pytest

import responses
import stripe

from ..factory import StripeMockAPI


@responses.activate
def test_customers():
    customer_id = 'cus_hihi'

    s = StripeMockAPI()

    s.add_customer(customer_id)
    s.sync()

    customer = stripe.Customer.retrieve(customer_id)
    assert customer.id == customer_id

    assert len(stripe.Customer.list()) == 1

    customer_404_id = 'cus_that_doesnt_exist'
    message = 'No such customer: {}'.format(customer_404_id)
    with pytest.raises(stripe.error.InvalidRequestError, message=message):
        stripe.Customer.retrieve(customer_404_id)


@responses.activate
def test_plans():
    s = StripeMockAPI()
    plan_id = 'my_special_plan'
    s.add_plan(plan_id)
    s.sync()

    plan = stripe.Plan.retrieve(plan_id)
    assert plan.id == plan_id

    assert len(stripe.Plan.list()) == 1

    plan_404_id = 'plan_that_doesnt_exist'
    message = 'No such plan: {}'.format(plan_404_id)
    with pytest.raises(stripe.error.InvalidRequestError, message=message):
        stripe.Plan.retrieve(plan_404_id)


@responses.activate
def test_subscriptions():
    s = StripeMockAPI()
    customer_id = 'cus_hihi'
    subscription_id = 'sub_CAmsLPVVHEQadsfd'
    s.add_subscription(customer_id, subscription_id)
    s.sync()

    subscription = stripe.Subscription.retrieve(subscription_id)
    assert subscription.id == subscription_id

    assert len(stripe.Subscription.list()) == 1

    subscription_404_id = 'sub_that_doesnt_exist'
    message = 'No such subscription: {}'.format(subscription_404_id)
    with pytest.raises(stripe.error.InvalidRequestError, message=message):
        stripe.Subscription.retrieve(subscription_404_id)


@responses.activate
def test_coupon():
    s = StripeMockAPI()
    coupon_id = 'my_coupon_thing'
    s.add_coupon(coupon_id)
    s.sync()

    coupon = stripe.Coupon.retrieve(coupon_id)
    assert coupon.id == coupon_id

    assert len(stripe.Coupon.list()) == 1

    coupon_404_id = 'coupon_that_doesnt_exist'
    message = 'No such coupon: {}'.format(coupon_404_id)
    with pytest.raises(stripe.error.InvalidRequestError, message=message):
        stripe.Coupon.retrieve(coupon_404_id)
