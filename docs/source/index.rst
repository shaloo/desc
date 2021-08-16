.. Puttshack POC1 documentation master file, created by
   sphinx-quickstart on Thu Aug  5 17:22:30 2021.

.. Puttshack documentation Poc1
   Author: Shaloo Shalini

Puttshack Cloud API Documentation
==================================

*Welcome to Puttshack Cloud API documentation!*

|product_name| offers an agile, scalable and responsive integration platform that can be used to build scalable products and services.

This documentation is targeted at *Puttshack Marketing Team* and *Developers* who intend to use |product_name| for enhancing Puttshack customer experience.

Here is how this documentation is organized:

**Getting Started Guide**:  This guide is intended to help build a :ref:`quick understanding<docref_puttshack_gsg>` of the |product_name|. It gives a brief product overview, highlights key components and building blocks, interaction mechanisms and product use model to enable new users onboard the product easily.

Here is a listing of some customer experiences and services that can be implemented using |product_name|:

.. include:: /common/ps_services.inc

**Use Cases**:  This document presents a  high level overview of :ref:`Key product use cases<docref_puttshack_uc>` such as enabling booking and reservations, modifying an already confirmed reservation, canceling a booking, purchasing or redeeming gift cards for Puttshack services etc.

**Workflows**:  Workflows refers to a collection of common API usage sequence. This document lists :ref:`Key API workflows<docref_puttshack_wf>` as simple flow chart diagrams for quick reference. The workflows capture a finer level of detail than the product use cases.  Some of the workflows may be common across several use cases. For example, :ref:`RSVP Workflow<ref_wf_rsvp>` may be common for event as well as gaming, food and drinks service booking use case. 

**API Reference**: Developers can find all low level details for each API in the :ref:`Puttshack API Reference Guide<docref_puttshack_apiref>`. It explains each API in terms of its expected inputs, input types, API response output and error codes that might show up. It is intended as a comprehensive reference book for creating various workflows that can be used to implement Puttshack services for various use cases.

.. toctree::
   :maxdepth: 2
   :caption: Contents
   :hidden:

   docs/gsg
   docs/usecases
   docs/workflows
   docs/api_ref
   docs/thirdp_prov
   docs/reports
   docs/concepts
