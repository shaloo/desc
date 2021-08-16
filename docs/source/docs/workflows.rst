.. _docref_puttshack_wf:
   
.. Puttshack documentation Poc1
   Author: Shaloo Shalini

.. spelling::

     mmd
     png

************************
Puttshack API Workflows
************************

.. warning::

     Please note only three workflows are populated as of Aug 11.  Rest will be done after initial feedback to avoid rework.

Workflow refers to a collection or unique set of API call sequences intended to achieve a specific objective related to a product use case. Some workflows may be commonly used across multiple use cases.

This document gives a brief overview of |product_name| workflows that can be used by Puttshack Developers to implement one or more Puttshack digital service offerings. Each workflow description comprises of a flow chart, followed by key stages of the workflow, error handling and a list of third party APIs used to implement the workflow.

Here is a list of API workflows covered in this document:

.. contents:: 
     :local:

----

.. _ref_wf_booking:

==================
Booking Workflow
==================

The Booking workflow enables creation of a reservation intent along with details such as location, number of players, courses, restaurant reservations for planning an event. It determines if a booking can be confirmed as a reservation based on availability and then initiate the payment workflow. 

Refer to the the booking flow chart below for details. Payment workflow details are available in the section titled :ref:`Payment Workflow<ref_wf_payment>`. The key stages and error handling for booking workflow are listed below:

.. figure:: /img/booking-workflow.png
   :align: center
   :width: 100%
   :figwidth: 95%
   :alt: booking_wf

   *Booking Workflow*

.. note::

     Double click on the flowchart to zoom in.

---------------------
Booking: Key Stages
---------------------

#. Use the booking details to check for reservation availability.

#. To reserve for 23 guests or less, then hold the reservation. 
   
   - If the reservation includes a course then request hold via Puttshack Reservation APIs. If reservation is confirmed then store details in :ref:`cloud database<ref_gsg_cloud_database>` and proceed with the :ref:`Payment Workflow<ref_wf_payment>`. If reservation is not confirmed, check whether restaurant reservation was successful, if not cancel the reservation and return 422 course error. 
     
   - If the reservation includes a restaurant, then request a hold via `Reservation APIs (TBD)<ref_tpa_opentable>`. If reservation is confirmed then store details in cloud database and proceed with the :ref:`Payment Workflow<ref_wf_payment>`. If reservation is not successful then cancel restaurant reservation and return 422 error.

#. To reserve for 24 guest or more, use Tripleseat APIs to store request details in Tripleseat and also update in cloud database. Return 200 success message and also share request details with Puttshack Sales Manager.

------------------------
Booking: Error Handling
------------------------

If the reservation is not successful for course booking, return 422 course error. Otherwise, if restaurant reservation was not successful, return 422 error.
Use webhooks to get notified of third party API call events that could result in reservation failure.

-------------------------------
Booking: Third Party APIs used
-------------------------------

* Event Management: 
  
  - Locations, Bookings via :ref:`Tripleseat<ref_tpa_tripleseat>`
  - Restaurant reservation for 23 guests of less via :ref:`Reservation API (Third Party)<ref_tpa_opentable>`
  - All service reservations beyond 23 guest via :ref:`Tripleseat<ref_tpa_tripleseat>`

.. _ref_wf_payment:

==================
Payment Workflow
==================

The Payment workflow enables processing of payment using third party API providers such as :ref:`Stripe<ref_tpa_stripe>`, while keeping various Puttshack booking related factors into account such as:

* Loyalty Points
* Perks offered
* Third party integration and cancellation

Refer to the the payment flow chart below for details. The key stages and error handling for payment workflow are listed below:

.. figure:: /img/payment-workflow.png
   :align: center
   :width: 100%
   :figwidth: 95%
   :alt: payment-wf

   *Payment Workflow*

.. note::

     Double click on the flowchart to zoom in.

---------------------
Payment: Key Stages
---------------------

#. The payment workflow is triggered from :ref:`Booking Workflow<ref_wf_booking>` . It needs reservation details, loyalty points as well as payment details before it can begin the Puttshack Cloud API Payment Confirmation process.

#. In case the discount is applicable, an appropriate amount is first deducted from payment details. Otherwise the payment is processed directly.  Payment processing is done via third party Stripe APIs.

#. If the third party payment fails, return 422 payment error as the Puttshack Confirm API endpoint call.

#. Once the payment is successful, confirm reservation and check what all options are included in the booking.

   - For course reservation, see if the Puttshack reservation API was successful and update reservation details in the cloud database. Otherwise, void the payment transaction, cancel the reservation (if it was implemented using `Reservation APIs (TBD)<ref_tpa_opentable>` based booking) and return 422 Puttshack confirmation error.

   - For restaurant reservation, see if reservation confirmation was received and update reservation details in the cloud database. Otherwise void the payment transaction, cancel the reservation (if it was a reservation based on `Reservation APIs (TBD)<ref_tpa_opentable>` booking) and return Puttshack confirmation error.

------------------------
Payment: Error Handling
------------------------

If the payment processing fails, cancel all the third party based reservations - `Reservation APIs (TBD)<ref_tpa_opentable>` ones for example.

Use webhooks to get notified of third party API call events that could result in payment failure.

-------------------------------
Payment: Third Party APIs used
-------------------------------

* Event Management: 
  
  - Restaurant reservation for 23 guests or less via :ref:`Reservation APIs (TBD)<ref_tpa_opentable>`

* Online Payments:

  - :ref:`Stripe<ref_tpa_stripe>` is used for online payment transactions 

.. _ref_wf_trieventconfirm_wb:

===============================================
Tripleseat Event Confirmation Webhook Workflow
===============================================

.. note:: Work in Progress...

      I did not get enough time yet to complete this workflow - TBD.

.. _ref_wf_upd_reservation:

============================
Update Reservation Workflow
============================

.. note:: Work in Progress...

      I did not get enough time yet to complete this workflow - TBD.

.. _ref_wf_rsv_notify:

===================================
Reservation Notifications Workflow
===================================

.. note:: Work in Progress...

      I did not get enough time yet to complete this workflow - TBD.

.. _ref_wf_rsv_seated:

============================
Reservation Seated Workflow
============================

.. note:: Work in Progress...

      I did not get enough time yet to complete this workflow - TBD.

.. _ref_wf_rsvp:

=============
RSVP Workflow
=============

The RSVP workflow is intended to enable the event or party host to invite other people as players or participants and track who has accepted the invite and will be attending the event.

Refer to the the RSVP flow chart below for details.  Key stages and error handling are for RSVP workflow are listed below:

.. figure:: /img/rsvp-workflow.png
   :align: center
   :width: 100%
   :figwidth: 95%
   :alt: toponav

   *RSVP Workflow*

.. note::

     Double click on the flowchart to zoom in.

----------------
RSVP: Key Stages
----------------

#. Ensure the event or reservation exists before invoking the next steps of the RSVP workflow.

#. Obtain the reservation details and check if the event host wishes to add other player or attendee details for RSVP processing.

#. If the event host chooses to add other player or attendee details, then obtain details from the cloud and generate a unique verification code. Store it for guest verification use later. Send the code via email/phone to each invited guest and track their response. 

#. Update the guest RSVP status information into the cloud database.

#. Notify the event host when attendees or other guests confirm their acceptance.

---------------------
RSVP: Error Handling
---------------------

If the event host chooses to update guest information for RSVP based response notification, an email / SMS is sent to each invitee.  If the email or SMS dispatch successful notification is not received from the third part API provider used for communication, text and email support, then return an error response.

----------------------------
RSVP: Third Party APIs used
----------------------------

* Communications: 
  
  - Emails via :ref:`Sendgrid<ref_tpa_sendgrid>`
  - SMS via :ref:`Twilio<ref_tpa_twilio>`
  - Utilize Promotional loyalty points and perks, enroll into Perks (new users) via :ref:`Punch<ref_tpa_punchh>`
