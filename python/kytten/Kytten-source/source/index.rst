.. Kytten documentation master file, created by
   sphinx-quickstart on Mon Aug 22 19:28:01 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Kytten's documentation!
==================================

Kytten is a Pyglet-based GUI library which aims to be easy to use and customizable.

.. toctree::
   :maxdepth: 2

Features
========

* Customizable!
* Dialogs are self-sizing and positioning!
* Widgets may be arranged vertically, horizontally, in a grid, or free form.
* Scrollable!

You can embed parts of the GUI within a scrollable area, allowing you to create very long menus or documents.

A simple theme editor allows you to create theme files with textures you provide. Textures may contain one or more graphics, you can then use the image region selector to define individual images in a texture, or set the stretchable parts of images that are designed to wrap content.

Simple GUI construction.
========================

Create a Dialog containing multiple widgets in one Python call! For example::

    dialog = kytten.Dialog(
        kytten.TitleFrame("Kytten Demo",
            kytten.VerticalLayout([
                kytten.Label("Select dialog to show"),
                kytten.Menu(options=["Document", "Form", "Scrollable"],
                            on_select=on_select),
            ]),
        ),
        window=window, batch=batch, group=fg_group,
        anchor=kytten.ANCHOR_TOP_LEFT,
        theme=theme)

Controls implemented so far:
============================

* Labels
* Text input fields
* Buttons
* Checkboxes
* Sliders
* Scrollbars
* Menus
* Untitled and titled frames
* Section headers and folding sections
* Dropdown menus
* FileLoadDialog and FileSaveDialog
* PopupMessage and PopupConfirm

Requirements
============

You'll need to update to pyglet 1.1.4 if you haven't already!

If you use a version of Python older than 2.6, simplejson will not be included in Python. kytten will try to use a safe_eval routine to process .json files.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

