.. _docref_puttshack_uc:

.. Puttshack documentation Poc1
   Author: Shaloo Shalini
   
*****************
Product Use Cases
*****************

This document highlights key product use cases that Puttshack business requires to be accomplished by using |product_name|.

These use cases also encapsulate the Puttshack customer stories or scenarios that need to be addressed eventually through these online service offerings.

For clarity, we have categorized these use cases into two distinct types: business and system use cases.

**Business** use case refers to the high level business task that is required to be addressed, whether it is driven from a customer use scenario or pure business need.  **System** use case refers to specific tasks and internal requirements that have to be accomplished by the product, |product_name|, in order to meet technical, internal system integration needs, marketing or developer requirements.

The following sections lists these use cases under the respective categories:

.. contents:: Use case categories
     :local:

----

===================
Business Use Cases
===================

* List available Puttshack locations
* Enable customer, kiosk operator initiated booking requests
* Allow viewing and update of player profiles
* Facilitate secure and fast online payments, cancellations
* Notify customers regarding conversion of booking to a confirmed reservation
* Enable customer to make changes to a reservation
* Perk enrollment, verification and redemption
* Gift Card purchase and redemption 
* Inventory

=================
System Use Cases
=================

* Locations

  - Obtain a list of current Puttshack locations from the information store
  - Update the information store when a new location needs to be registered via some trigger.

* Bookings

  - List available bookings for a specified date / time.
  - Create a fresh booking request.
  - Obtain a booking details.
  - Update or change a booking.
  - Show list of reservations for a unique booking identification sequence.
  - Notify a customer once the booking is confirmed.

* Players

  - List all players registered for a booking.
  - Create a new player.
  - Update a players profile.
  - Notify a player for a score update

* Payments

  - Initiate a payment through intent
  - Obtain and update payment intent status via third party webhook integration
  - Maintain payment status, correlation with reservation, customer or player identification, booking, Puttshack service usage history.
  - Notify customer with payment status.
  - Integrate payment status with player perks based on promotions and third party webhooks.

* Reservations

  - List all reservations for a given date/time or for a customer, player.
  - Search for a booking and track status if it was confirmed as a reservation or not.
  - Enable prior reservations to be updated.
  - Log all changes to a reservation, who made it and when, what was changed.
  - Track reservation patterns across locations, players, Puttshack services.

* Perks

  - Enable Perk sign up by customers. 
  - Verify Perk sign up (email/phone).
  - Integrate perk with player transactions and service usage.
  - Integrate perk with promotion notifications (if opted-in).

* Inventory

  - List all inventory.
  - Update inventory.

* System Reports

  - Active users report to track active users, number of visits, services availed in a specified time frame.
  - Sales / Finance report with statistics related to transactions per location, total sales, total refunds, total taxes, average revenue per booking, most popular and least popular service offerings or packages.
  - Email delivery report listing email deliver statistics and engagements in case of promotional or transaction events.
  
.. warning::

     Does this level of detail suffice to begin with or do we need to expand it further for each use case, say in terms of:

     * Use case name
     * description
     * prerequisites
     * flows
     * exceptions
     * post-conditions
     * events or triggers

     In the case of the latter (more details required), I'll need follow up calls with Chris to capture these insights in detail = more time, effort, resources. Hence the query/confirmation before going ahead in this direction.
