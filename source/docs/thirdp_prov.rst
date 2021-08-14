.. _docref_puttshack_thirp_details:

.. Puttshack documentation Poc1
   Author: Chris Moore, Shaloo Shalini

.. spelling::

     booker
     Checkins
     redemptions
     transactional

**************************
Third Party API Providers
**************************

This document provides a consolidated list of all third party API providers used to implement |product_name|.

.. contents:: 
     :local:
     :depth: 2

----

Perks and Accommodations
========================

.. _ref_tpa_tripleseat:

Tripleseat
----------

The Tripleseat API will be utilized when parties of 12 or more book a
reservation.

**Locations API**

PSC will pull location details down from Tripleseat and store the
information in the PSC database. Doing so will allow PSC to associate
booking requests with locations created in the Tripleseat dashboard.

-  `Locations
   Documentation <https://support.tripleseat.com/hc/en-us/articles/212570457-Locations-API>`__

**Leads API**

When a booking of 12+ is requested, PSC will create a new Lead via the
Tripleseat API. For reservations of < 24 guests, this will include
booking and payment details.

-  `Leads
   Documentation <https://support.tripleseat.com/hc/en-us/articles/212528787-Leads-API>`__

**Webhooks**

Tripleseat sends out webhooks for updates to Leads and Events. The PSC
will register to these hooks and will update the contents stored in the
PSC database when events are sent over due.

-  `Webhooks
   Documentation <https://support.tripleseat.com/hc/en-us/articles/360002146094-Tripleseat-Webhooks>`__

**Additional References**

-  `API Documentation
   Site <https://support.tripleseat.com/hc/en-us/articles/205162108-API-Overview-Getting-Started>`__

----

.. _ref_tpa_punchh:

Punchh
------

The Punchh API will be utilized to store Perk membership sign ups,
calculate and redeem perks, and attaching transactions to loyalty
members for reporting purposes.

**User API**

When a user chooses to sign up for a Perks membership, PSC will send
over the lead booker’s information to store as a new user in the Punchh
Platform. The loyalty membership ID will be stored in the PSC database
for reference.

-  `Create new user
   documentation <https://developers.punchh.com/pos-apis/point-of-sale/pos-create-user>`__

**Checkin API**

Punchh Checkins are used to track purchases members should receive
points/redemptions/offers for. When a payment transaction is completed,
PSC will look to see if a Punchh membership is associated with the
account and if so, a new ``checkin`` will be created in the Punchh
system.

-  `Create
   Checkin <https://developers.punchh.com/pos-apis/point-of-sale/pos-checkin>`__

**Redemptions API**

When PSC calculates a payment total for a purchase, it will first check
to see if the user is already a Punchh member (references the
``users.punchh_id`` database column and checks to see if it has a value)
and if so it will check to see if any redemptions are available for the
member. If a redemption is available, it will show up as a line item in
the payment details.

If the member chooses to use a redemption and completes a purchase, PSC
will update the redemption status in Punchh.

If a payment is refunded or voided, PSC will lookup the associated line
items and if a redemption is attached to the payment, PSC will send a
void request to the Punchh API.

-  `Check Possible
   Redemptions <https://developers.punchh.com/pos-apis/point-of-sale/pos-redemption-possible>`__
-  `Create
   Redemption <https://developers.punchh.com/pos-apis/point-of-sale/pos-create-redemption>`__
-  `Void
   Redemption <https://developers.punchh.com/pos-apis/point-of-sale/pos-void-redemption>`__

**Additional References**

-  `API Docs Homepage <https://developers.punchh.com/core-api-docs>`__

----


Payments
========

.. _ref_tpa_stripe:

Stripe
------

Stripe will be used to handle all payment transactions processed by PSC.
Stripe also provides a dashboard to allow admin users to void
transactions or issue refunds. To assist in PCI-compliance, Stripe can
be used to render the credit card portion of a form and will send a
transaction key to the PSC server to verify that a payment was
successful or unsuccessful.

**Payment Intents**

When a user hits the payment section of the booking flow, the CC form
details and payment will be handled by Stripe. Once the payment has been
processed (or denied), Stripe will provide payment details which will be
sent to the PSC server to store for transactional history.

-  `Payment Intent
   Flow <https://stripe.com/docs/payments/integration-builder>`__

**Webhooks**

Stripe provides webhooks for updated payment information. If an admin
voids or refunds a payment, Stripe will send the details to PSC so the
payment details can be updated in the cloud database to keep payment
history updated.

----

Communications
==============

.. _ref_tpa_twilio:

Twilio
------

Twilio’s API will be used to send out verification emails from the PSC
system when a member chooses to sign up for a Perks membership or
attempts to sign in.

To get notifications sent out via the API as quickly as possible, a
scalable PSC endpoint will be utilized so multiple SMS messages from the
same location can be sent out in parallel without the need to create a
queue that could possibly delay messages.

**Additional References**

-  `Send Message API <https://www.twilio.com/docs/sms/send-messages>`__
-  Scalable Services

   -  `Google Cloud Pub/Sub <https://cloud.google.com/pubsub>`__
   -  `AWS Simple Queue Service (SQS) <https://aws.amazon.com/sqs/>`__

----

.. _ref_tpa_sendgrid:

SendGrid
--------

SendGrid is used to send out email communications to guests and/or perks
members.

**Sending Mail**

SendGrid allows its users to create email templates inside their
dashboard. These templates can be stored so they may be used for
outgoing messages from PSC. Additional details from PSC can be sent to
fill in dynamic data such as the user’s name, game scores, etc.

-  `Mail Send
   (Template) <https://docs.sendgrid.com/api-reference/mail-send/mail-send>`__

**Webhooks**

SendGrid has webhooks for event tracking for emails sent out through
their platform. These updates can be used to track if an individual has
unsubscribe from a campaign, sent the email to spam, or if an email
address is invalid (hard-bounce).

-  `Enable/Disable
   Webhooks <https://docs.sendgrid.com/api-reference/webhooks/enabledisable-signed-webhook>`__
-  `Event Webhook
   overview <https://docs.sendgrid.com/for-developers/tracking-events/getting-started-event-webhook>`__

**Additional References**

-  `Retrieve Template
   HTML <https://docs.sendgrid.com/api-reference/transactional-templates/retrieve-a-single-transactional-template>`__

----

Point of Sales 
==============

.. _ref_tap_focus_tevalis:

Focus / Tevalis
-----------------

Both FocusPOS and TevalisPOS provides methods to open a check via their
API. Depending on the reservation system selected, integration with
these POS systems may already be provided.

However, if not, when PSC gets and update through the reservation system
that a reservation has been sat, it can open a check in the POS system
automatically.

-  `FocusPOS - Open a
   Check <https://api.focuspos.com/#43331c3f-aa89-4bcb-860e-e14a83afc6dd>`__
-  `Tevalis - Create Reservation (Open a
   Table) <https://api.tevalis.com/Help/Api/POST-Reservation-CreateReservation-SiteID>`__

----

Gift Cards
==========

.. _ref_tpa_focus_giftpro:

FocusGift / GiftPro
--------------------

FocusGift and GiftPRo provides an API to handle gift card transactions.
When a U.S. based customer enters a gift card number at checkout, PSC
will make a request to the FocusGift API to check the balance.
Alternatively, if the customer is U.K. based, a request will be made to
the GiftPro API. If a balance exists, the total will be deducted from
the customer’s purchase.

-  `FocusGift
   API <https://help.focusca.com/hc/en-us/articles/360040732172-FocusGift-API-Activating-Cards>`__
   - *Note: Prior to integration, PSC will need to become a FocusGift
   integrator as mentioned in the docs*
-  `GiftPro API <https://www.giftpro.co.uk/api/>`__ - Note: A
   integration key must be granted prior to integration with the GiftPro
   API

**Additional Resources**

-  `Tevalis API Docs <https://api.tevalis.com/Help>`__
-  `FocusPOS API Docs <https://api.focuspos.com/#intro>`__

----

Restaurant Reservation
=======================

.. _ref_tpa_opentable:

OpenTable
----------

.. note::

     This info was not available in original document where other third party providers were listed as of Aug 9. So I can fill in this detail if OpenTable is confirmed as one of the 3rd party APIs that Puttshack Cloud APIs are using.  I found OpenTable reference in the Miro board workflow. So adding it here in the list for completeness.
