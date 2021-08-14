.. _docref_puttshack_reports:

.. Puttshack documentation Poc1
   Author: Shaloo Shalini

.. spelling::
     
      TBD

*********
Reports
*********

|product_name| reports  are meant to help you understand and reconcile the activity in Puttshack Cloud information store, analyze event and party host user actions, service usage and much more. You can view summary reports once there is enough data collected and slice, dice the data for business insights. 

========
Overview
========

|product_name| has a cloud based component that acts as the information store, known as Cloud Database (DB). This component is structured to store information in a database which can be used to handle daily processes (such as RSVP reminders), displaying profile information to users and reporting for Puttshack personnel. This documents provides an overview of the types of reports that can be generated with the current DB structure.

.. contents:: Types of Reports
     :local:

----

-------------------
Active User Reports
-------------------

Based on a range determined by Puttshack (i.e., 30 days), a report can be generated to showcase how many users were active within a given time period, the average amount of visits, and total visits per user.

---------------
Finance Reports
---------------

Financial reports can be generated to provide an overview of transactions which took place in any of the Puttshack venues. Reports such as total sales, total refunds, total taxes, average revenue per booking and most popular packages can be generated with the payment details stored in the PSC database.

----------------------
Email Delivery Reports
----------------------

Email delivery reports can be generated to provide insights into email delivery statistics based on third party API services used for communications. The data corresponding to such email deliveries is tracked using webhooks that are triggered when an email transaction occurs.

=======
Future
=======

In future, based on Puttshack requirements, additional categories of reports may be implemented and available for use.
