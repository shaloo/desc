.. _docref_puttshack_gsg:

.. Puttshack documentation Poc1
   Author: Shaloo Shalini

.. spelling::

      booker

*********************
Getting Started Guide
*********************

|product_name| are REST based interfaces that require API specific encoded request inputs and return JSON-encoded responses. Standard http response codes and verbs are used to implement |product_name|.

This guide helps you get a quick overview of how Puttshack Cloud APIs can be used to develop digital products for Puttshack customers that are accessible as online service offerings.  In addition, these APIs can also be utilized to create an administrative dashboard or internal apps meant for internal use, by sales and marketing teams. The administrative interface can be used to track customer transactions, analyze service usage patterns, identify gaps in offerings as well as customer experience levels, response times and more.

.. contents:: Getting Started
     :local:

----

=========
Overview
=========

|product_name| offer several categories of endpoints geared towards enabling various Puttshack services. Each service is built using one or more API workflows depending upon the service use case.  A workflow refers to a unique and well defined sequence of specific Puttshack API requests, followed by response handling and subsequent calls to the same or another bunch of APIs.

The APIs can be invoked using tools such as Postman that refers to a test server deployment. Alternatively, these can also be invoked indirectly through a  web based application. The |product_name| are built using REST API practices and several well-known third party APIs that are secure, scalable and used by various other businesses.

In the following sections, you will learn about Puttshack Online customer offerings, |product_name| functionality overview, various categories of |product_name| that can be used to create workflows and implement Puttshack services and offerings using these APIs. You can take a peek under the hood into the ecosystem powered by |product_name| such as, how it works, what third party APIs are used internally, how are notifications managed asynchronously through webhooks, the kind of customer data that is stored in the cloud database and can be used for business insights and analytics, etc.

.. _ref_gsg_dig_offerings:

==================
Digital Offerings
==================

Typically, Puttshack customer touch points involve web, kiosk and gaming. The Puttshack website or kiosk can be used to perform any of these actions:

.. include:: /common/ps_customer_actions.inc

Every customer expects acceptable response time and transaction guarantees for these actions. Puttshack can use |product_name| to implement their offerings or services to address customer demands.  |product_name| are designed keeping customer experience in mind. The idea is to enhance Puttshack customer experience such that they feel encouraged to use other Puttshack offerings as well, driven by a seamless, enjoyable experience, enhanced by technology rather than inhibited by service delays and errors.

|product_name| can be used to implement the following Puttshack offerings (and may be more in future):

.. include:: /common/ps_services.inc

.. _ref_gsg_how_it_works:

=============
How it works?
=============

This section provides a high level overview of various components that make up Puttshack Cloud API ecosystem, their interactions and the use model.

To address the customer requirements and Puttshack offerings listed in the :ref:`Digital Offerings<ref_gsg_dig_offerings>` section above, |product_name| offers the following categories of APIs:

.. _ref_prod_api_categories:

--------------
API Categories
--------------

.. include:: /common/api_categories.inc

.. note::

     To begin with, |product_name| Categories listed above are offered. In future, these may evolve to additional API categories depending upon Puttshack requirements.

---------
Use Model
---------

The Puttshack customers do not directly interact with the APIs.  They use the web applications, mobile apps or kiosk apps built by Puttshack IT Team and Developers. These applications offer various Puttshack services and use |product_name| to implement various use cases through :ref:`API workflows<docref_puttshack_wf>`.  The Puttshack Management team could use these APIs for reports and analytics and gathering Puttshack service usage insights and financial transaction patterns.  Alternately, the Puttshack IT Team and Developers could create in-house reporting apps that are tailored for Puttshack Management Team instead of having to invoke APIs for reports.

.. _ref_gsg_sys_comp:

-----------------
System Components
-----------------

Figure below gives a quick snapshot of various components involved, their interactions and how the |product_name| actually work under the hood.  

.. note::

      Double click on the image to zoom in.

.. figure:: /img/how_it_works.png
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: How-it-works

   *Under the hood: Key components and interactions*

You can see three kinds of user entities that interact with the services in this ecosystem:

#. **Puttshack Management Team**:  Puttshack Management team refers to personnel from Marketing, Operations & Finance and Sales teams who are interested in utilizing Puttshack Cloud APIs. This team typically defines Puttshack digital products or suggests improvisations in existing products, tracks reports of service usage.

#. **Puttshack IT Team & Developers**: This team is in charge of implementing Puttshack digital service offerings based on definitions from the management team. It leverages |product_name| to implement these definitions as customer facing or internal applications.

#. **Puttshack customers**:  Avails of various Puttshack offerings through the website or kiosk.

There are five key components in the core Puttshack ecosystem:

*  Management/Developer Access:
*  The Cloud APIs  
*  The Cloud Database (Information Store)
*  Third Party APIs
*  Webhook Integration for Third Party API notification management

Let us take a closer look at each of these components and how they interact with each other.

---------------------------
Management/Developer Access
---------------------------

The Management and Developer access refers to the interaction of Puttshack team with the |product_name|. The primary mechanism of interaction with |product_name| is through the endpoints. The interactions can be direct or indirect. Developers typically interact directly  with the endpoints as they use these APIs for implementing applications that are used by Puttshack customers eventually.  Management team folks can choose to interact directly via reporting APIs or indirectly through in-house web applications created by the developers using these same APIs.

-----------
Cloud APIs
-----------

Earlier, the document listed :ref:`various categories<ref_prod_api_categories>` of |product_name| that can be utilized by Puttshack IT Teams, Marketing, Operations, Sales and Finance.  Each of those categories contains several API endpoints. Cloud API is a self contained component that offers several  **endpoints** as building blocks for Puttshack services. It integrates with third party APIs, stores customer, service usage, location, booking, reservation, player, payments, perks, customer preferences and other related information in a cloud based datastore. 

The Cloud API component uses webhooks to update information received regarding various service triggered API calls locally and provides that information when requested by the Puttshack service invoked by a customer action. Besides these functions, it acts as a storehouse or treasure trove of sorts that can be leveraged for rich business and marketing insights through reports and analytics. 

The Cloud API component implements Puttshack Cloud API endpoints and they are deployed on a server. This :ref:`PSC<ref_c_PSC>` subsystem is referred to as :ref:`PSC<ref_c_PSC>` in this documentation. Through webhook integration, various third party API providers can notify :ref:`PSC<ref_c_PSC>` server about various events such as successful payment, successful reservation processing, enrolling into loyalty and perks via a third party etc.  When these notifications are received, they are stored in the `Cloud Database<ref_gsg_cloud_database>`.

.. note::

     As there is no Admin dashboard, the webhook integration cannot be configured by Developers directly as of now.  The webhook bindings are taken care of in the Cloud API component. It may or may not be configurable via external interfaces as of now.

.. _ref_gsg_cloud_database:

---------------
Cloud Database
---------------

The |product_name| use a cloud Database as its information store.  This database stores several pieces of important information related to various Puttshack service transactions such as bookings, players, locations, payment correlation etc. Another route through which this cloud database is accessed and updated are the webhook integration. The webhook integration of |product_name| with third party APIs results in certain notifications that require update in status or changes in the information stored in the cloud database.  

All the database operations and handling is managed by the Cloud API component. None of the customer can get an access to this internal, private information store directly.  They can only access online service offerings to read information that they are allowed to. For example, reservation details and perks.  When Puttshack customers use the online service offerings, their actions indirectly drive the database updates through workflows and service use cases implemented by Puttshack Developers and IT Team.  Only Puttshack IT Team and Developers have direct access to this cloud database.

Figure below shows a sample of the cloud database schema and kinds of data that is stored, maintained therein.

.. figure:: /img/ps_info_store_schema.png
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Cloud db schema

   *Details: Information Store Database Schema*

.. note::

     This is not the final schema but a working copy of the current implementation, subject to change.

Next, we take a look at the third party API providers that are used by Cloud API component to render various workflows and endpoint functions.

---------------------
Third Party Providers
---------------------

|product_name|  utilizes various third party APIs to create workflows that can be used to build various Puttshack services.  The reason behind utilizing industry proven third party APIs is to ensure that Puttshack services are backed by scalable, responsive and efficient functionality offered by widely used by reliable API providers without spending unnecessary re-engineering effort where not required.

The following table list the third party API Providers that are utilized by Puttshack Cloud APIs:

.. include:: /common/ps_third_p.inc

.. _ref_gsg_wbh_int:

-------------------
Webhook Integration
-------------------

Webhooks are mechanisms used by most third party API Providers to notify the API users when an event happens related to an account's API usage. These events are asynchronous, say for example, a payment APIs a webhook may be invoked if a bank confirms the payment, or when returning players verify their phone number or email.

Webhook integration involves the following steps:

* Defining a webhook endpoint at the Puttshack Cloud API server
* Using the third party CLI to test invoke it
* Registering the webhook with the third party provider for live/production setup

Once the webhook is registered, the third party provider will notify Cloud APIs component when an event for which webhook was registered actually occurs. The webhook action taken by the Cloud API component may vary depending upon the kind of event. For example:

* Update a customers perk enrollment status once they verify and opt-in.
* Make adjustments to an invoice when it is created to accommodate gift cards or perks.
* Update and link booking to a reservation once it is confirmed and notify the customer.

In future, webhooks can also be used to provide cloud database state and API responses to Puttshack internal services or systems that need to be integrated and use customer data for services such as replication, analytics, or alerting.

^^^^^^^^^^^^^^
Why Webhooks?
^^^^^^^^^^^^^^

Most of the third party APIs are invoked in response to either a customer action or another API call as part of a service's workflow. The response to a request is immediately received and acted upon. The action may result in invoking another API or the same API.  However, there are cases when asynchronous events need to be communicated by the third party service provider to the service user - Puttshack Cloud API component, in this case. These asynchronous events require some action by the service user such as update in state, notify its users in turn or add new information, alerts in the Puttshack ecosystem.

.. _ref_gsg_sys_proc:

================
System Processes
================

Puttshack Cloud APIs are implemented as REST APIs. Besides the :ref:`system components<ref_gsg_sys_comp>` listed above, including the :ref:`webhook integration<ref_gsg_wbh_int>` and :ref:`cloud database<ref_gsg_cloud_database>`, there are various processes that do the background and housekeeping tasks in response to API invocations and webhook calls.  These processes are referred to as the **Daily Processes** described below:

.. _ref_gsg_daily_proc:

---------------
Daily Processes
---------------

Following are the daily processes that run in the background and gather system information and updates:

.. contents::  
     :local:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Locations, Player Types and Opening Times
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`PSC<ref_c_PSC>` will have a bunch of daily processes that run on a daily basis to gather the latest information for locations, player types and opening times. Because these items rarely change, the amount of network requests can be reduced by storing such rarely changing  information in the cloud database itself and serving it directly when requested by the Puttshack Kiosk an`d web application.

^^^^^^^^^^^^^^^^^^^^
Reconciling Booking
^^^^^^^^^^^^^^^^^^^^

The :ref:`PSC<ref_c_PSC>` daily process will cycle through all the bookings created during the day. It can utilize the `searchBooking` and/or `getBooking` endpoints to reconcile any updates made in the Puttshack admin that may not have been provided to the :ref:`PSC<ref_c_PSC>` system.

^^^^^^^^^^^^^^
Game Details
^^^^^^^^^^^^^^

On an hourly basis, the :ref:`PSC<ref_c_PSC>` daily process will cycle through (past) bookings and make a request to the `/Games/{bookingId|bookingRef}` endpoint to obtain score card details for associated guests.

.. note::

     *Not required with Puttshack Web Hooks*

---------------
Other Processes
---------------

Unlike the :ref:`daily system processes<ref_gsg_daily_proc>`, the following system processes are initiated in response to the Puttshack Cloud API invocations.

.. contents::  
     :local:

^^^^^^^^^^^^^^
Booking Flow
^^^^^^^^^^^^^^

Following processes will manage gathering information and storing it in cloud database when the booking related Puttshack Cloud API endpoints are invoked:

"""""""""""""""""""""
Availability Request
"""""""""""""""""""""

:ref:`PSC<ref_c_PSC>` will internally use the endpoint ``POST /GetAvailability`` to submit an availability request through a venue's Kiosk or web application. It will then use the output provided by the API to display potential playing times available to the end user to select.

**Additional Requirements:** The Puttshack API will need to accept number of guests and games so only one request needs to be made to obtain available time slots.

"""""""""""""""""""""""
Create Booking Request
"""""""""""""""""""""""

Once a user has selected a time slot and number of guests/players, the :ref:`PSC<ref_c_PSC>` will use the ``POST /BookingRequest`` to submit the user's request and obtain booking options. The user will have 8 minutes from this time to complete their booking flow, otherwise the same booking request will be re-attempted on the user's behalf. If the booking request is unsuccessful, it will display an error to the end user.

"""""""""""""""""""""""
Confirm Booking Request
"""""""""""""""""""""""

Once a user has completed the booking process on :ref:`PSC<ref_c_PSC>` and successfully paid for their reservation, it will use the ``POST /BookingConfirm`` endpoint to confirm a booking. If an error occurs at this stage, the payment transaction will be voided an error will display to the user.

^^^^^^^^^^^^^^
Booking Update
^^^^^^^^^^^^^^

Following processes handle the booking updates or changes:

"""""""""""""""""""""
Booking Cancellations
"""""""""""""""""""""

If a user chooses to cancel their booking the :ref:`PSC<ref_c_PSC>`  will send a ``POST /BookingCancel`` request to the endpoint with the original Booking identifier and price provided by the Puttshack cloud database.

"""""""""""""""""
Booking Updates
"""""""""""""""""

If a user chooses to update booking details :ref:`PSC<ref_c_PSC>` will send a ``POST /BookingEditRequest`` request to the endpoint which will include the updated booking details. The returned details will be used to show the user and differences in pricing. If additional funds need to be obtained, :ref:`PSC<ref_c_PSC>` will charge the user for the difference.  If the payment is success it will send a ``POST BookingEditConfirm`` request to the endpoint to mark the edited details as confirmed.

^^^^^^^^^^^^^^
Guest RSVP
^^^^^^^^^^^^^^

"""""""""""""""""""""
Booking Guest Details
"""""""""""""""""""""

When the lead booker or the guest that hosts an event, updates their information :ref:`PSC<ref_c_PSC>` will send a ``POST /BookingGuestDetails`` request to update guest information.

================
More Information
================

This guide provides an overview of |product_name|, its usage, how it works and key components involved. For further information, refer to the following documentation:

- :ref:`Product Use Cases<docref_puttshack_uc>`
- :ref:`Product Workflows<docref_puttshack_wf>`
- :ref:`Puttshack API Reference Guide<docref_puttshack_apiref>`
