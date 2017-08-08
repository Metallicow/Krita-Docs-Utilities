#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utilities for downloading MediaWiki docs for offline use for the application "Krita"
https://docs.krita.org

* Download MediaWiki markup contents
* Download MediaWiki pdf exports
* Shitty files conversion(only does some files) mediawiki to rst with pandoc(https://pandoc.org/)

You may need to be logged in for these to work...

"""

import os
import sys
import subprocess
import urllib2
from collections import OrderedDict


PAGE_LINKS = OrderedDict([
    # ("Main page",    "https://docs.krita.org/index.php?title=Main_Page"),

    ("User Manual",                                                 "https://docs.krita.org/index.php?title=Category:User_Manual"),
        ("Getting Started",                                         "https://docs.krita.org/index.php?title=Category:Getting_Started"),
            ("Introduction coming from other software",             "https://docs.krita.org/index.php?title=Category:Introduction_coming_from_other_software"),
                ("Introduction to Krita coming from Painttool Sai", "https://docs.krita.org/index.php?title=Introduction_to_Krita_coming_from_Painttool_Sai"),
                ("Introduction to Krita coming from Photoshop",     "https://docs.krita.org/index.php?title=Introduction_to_Krita_coming_from_Photoshop"),
            ("Installation",                                        "https://docs.krita.org/index.php?title=Installation"),
            ("Starting Krita",                                      "https://docs.krita.org/index.php?title=Starting_Krita"),
            ("Basic Concepts",                                      "https://docs.krita.org/index.php?title=Basic_Concepts"),
            ("Navigation",                                          "https://docs.krita.org/index.php?title=Navigation"),
        ("Animation",                                               "https://docs.krita.org/index.php?title=Animation"),
        ("Drawing Tablets",                                         "https://docs.krita.org/index.php?title=Drawing_Tablets"),
        ("Introduction to Layers and Masks",                        "https://docs.krita.org/index.php?title=Introduction_to_Layers_and_Masks"),
        ("Japanese Animation Template for Krita",                   "https://docs.krita.org/index.php?title=Japanese_Animation_Template_for_Krita"),
        ("Loading and Saving Brushes",                              "https://docs.krita.org/index.php?title=Loading_and_Saving_Brushes"),
        ("Mirror Tools",                                            "https://docs.krita.org/index.php?title=Mirror_Tools"),
        ("On Canvas Brush Editor",                                  "https://docs.krita.org/index.php?title=On_Canvas_Brush_Editor"),
        ("Painting With Assistants",                                "https://docs.krita.org/index.php?title=Painting_With_Assistants"),
        ("Selections",                                              "https://docs.krita.org/index.php?title=Selections"),
        ("Snapping",                                                "https://docs.krita.org/index.php?title=Snapping"),
        ("Soft Proofing",                                           "https://docs.krita.org/index.php?title=Soft_Proofing"),
        ("Tag System",                                              "https://docs.krita.org/index.php?title=Tag_System"),
        ("Templates",                                               "https://docs.krita.org/index.php?title=Templates"),
        ("Working with Images",                                     "https://docs.krita.org/index.php?title=Working_with_Images"),

    ("General Concepts",                                            "https://docs.krita.org/index.php?title=Category:General_Concepts"),
        ("Color",                                                   "https://docs.krita.org/index.php?title=Category:Color"),
            ("Bit Depth",                                           "https://docs.krita.org/index.php?title=Bit_Depth"),
            ("Color Managed Workflow",                              "https://docs.krita.org/index.php?title=Color_Managed_Workflow"),
            ("Color Models",                                        "https://docs.krita.org/index.php?title=Color_Models"),
            ("Color space size",                                    "https://docs.krita.org/index.php?title=Color_space_size"),
            ("Gamma and Linear",                                    "https://docs.krita.org/index.php?title=Gamma_and_Linear"),
            ("Mixing Colors",                                       "https://docs.krita.org/index.php?title=Mixing_Colors"),
            ("Profiling and Callibration",                          "https://docs.krita.org/index.php?title=Profiling_and_Callibration"),
            ("Scene Linear Painting",                               "https://docs.krita.org/index.php?title=Scene_Linear_Painting"),
            ("Viewing Conditions",                                  "https://docs.krita.org/index.php?title=Viewing_Conditions"),
        ("File Formats",                                            "https://docs.krita.org/index.php?title=Category:File_Formats"),
            ("*.bmp",                                               "https://docs.krita.org/index.php?title=*.bmp"),
            ("*.csv",                                               "https://docs.krita.org/index.php?title=*.csv"),
            ("*.exr",                                               "https://docs.krita.org/index.php?title=*.exr"),
            ("*.gbr",                                               "https://docs.krita.org/index.php?title=*.gbr"),
            ("*.gif",                                               "https://docs.krita.org/index.php?title=*.gif"),
            ("*.gih",                                               "https://docs.krita.org/index.php?title=*.gih"),
            ("*.jpg",                                               "https://docs.krita.org/index.php?title=*.jpg"),
            ("*.kra",                                               "https://docs.krita.org/index.php?title=*.kra"),
            ("*.ora",                                               "https://docs.krita.org/index.php?title=*.ora"),
            ("*.pbm",                                               "https://docs.krita.org/index.php?title=*.pbm"),
            ("*.pdf",                                               "https://docs.krita.org/index.php?title=*.pdf"),
            ("*.pgm",                                               "https://docs.krita.org/index.php?title=*.pgm"),
            ("*.png",                                               "https://docs.krita.org/index.php?title=*.png"),
            ("*.ppm",                                               "https://docs.krita.org/index.php?title=*.ppm"),
            ("*.psd",                                               "https://docs.krita.org/index.php?title=*.psd"),
            ("*.svg",                                               "https://docs.krita.org/index.php?title=*.svg"),
            ("*.tiff",                                              "https://docs.krita.org/index.php?title=*.tiff"),
        ("Projection",                                              "https://docs.krita.org/index.php?title=Category:Projection"),
            ("Projection: Orthographic and Oblique",                "https://docs.krita.org/index.php?title=Projection:_Orthographic_and_Oblique"),
            ("Projection: Axonometric",                             "https://docs.krita.org/index.php?title=Projection:_Axonometric"),
            ("Projection: Perspective",                             "https://docs.krita.org/index.php?title=Projection:_Perspective"),
            ("Projection: Practical Uses",                          "https://docs.krita.org/index.php?title=Projection:_Practical_Uses"),

    ("Reference Manual",                                            "https://docs.krita.org/index.php?title=Category:Reference_Manual"),
        ("Brushes",                                                 "https://docs.krita.org/index.php?title=Category:Brushes"),
            ("Brush Engines",                                       "https://docs.krita.org/index.php?title=Category:Brush_Engines"),
                ("Bristle",                                         "https://docs.krita.org/index.php?title=Bristle"),
                ("Chalk",                                           "https://docs.krita.org/index.php?title=Chalk"),
                ("Clone",                                           "https://docs.krita.org/index.php?title=Clone"),
                ("Color Smudge",                                    "https://docs.krita.org/index.php?title=Color_Smudge"),
                ("Curve",                                           "https://docs.krita.org/index.php?title=Curve"),
                ("Deform",                                          "https://docs.krita.org/index.php?title=Deform"),
                ("Dyna",                                            "https://docs.krita.org/index.php?title=Dyna"),
                ("Filter",                                          "https://docs.krita.org/index.php?title=Filter"),
                ("Grid",                                            "https://docs.krita.org/index.php?title=Grid"),
                ("Hatching",                                        "https://docs.krita.org/index.php?title=Hatching"),
                ("Particle",                                        "https://docs.krita.org/index.php?title=Particle"),
                ("Pixel",                                           "https://docs.krita.org/index.php?title=Pixel"),
                ("Quick Brush",                                     "https://docs.krita.org/index.php?title=Quick_Brush"),
                ("Shape",                                           "https://docs.krita.org/index.php?title=Shape"),
                ("Sketch",                                          "https://docs.krita.org/index.php?title=Sketch"),
                ("Spray",                                           "https://docs.krita.org/index.php?title=Spray"),
                ("Tangent Normal",                                  "https://docs.krita.org/index.php?title=Tangent_Normal"),
            ("Brush Settings",                                      "https://docs.krita.org/index.php?title=Category:Brush_Settings"),
                ("Spray",                                           "https://docs.krita.org/index.php?title=Spray"),
                ("Brush Tips",                                      "https://docs.krita.org/index.php?title=Brush_Tips"),
                ("Locked Brush Settings",                           "https://docs.krita.org/index.php?title=Locked_Brush_Settings"),
                ("Opacity & Flow",                                  "https://docs.krita.org/index.php?title=Opacity_%26_Flow"),
                ("Parameters",                                      "https://docs.krita.org/index.php?title=Parameters"),
                ("Sensors",                                         "https://docs.krita.org/index.php?title=Sensors"),
                ("Texture",                                         "https://docs.krita.org/index.php?title=Texture"),
        ("Dockers",                                                 "https://docs.krita.org/index.php?title=Category:Dockers"),
            ("Add Shape",                                           "https://docs.krita.org/index.php?title=Add_Shape"),
            ("Advanced Color Selector",                             "https://docs.krita.org/index.php?title=Advanced_Color_Selector"),
            ("Animation Curves",                                    "https://docs.krita.org/index.php?title=Animation_Curves"),
            ("Animation Docker",                                    "https://docs.krita.org/index.php?title=Animation_Docker"),
            ("Artistic Color Selector",                             "https://docs.krita.org/index.php?title=Artistic_Color_Selector"),
            ("Brush Presets",                                       "https://docs.krita.org/index.php?title=Brush_Presets"),
            ("Channels",                                            "https://docs.krita.org/index.php?title=Channels"),
            ("Color Sliders",                                       "https://docs.krita.org/index.php?title=Color_Sliders"),
            ("Compositions",                                        "https://docs.krita.org/index.php?title=Compositions"),
            ("Digital Color Mixer",                                 "https://docs.krita.org/index.php?title=Digital_Color_Mixer"),
            ("Grids and Guides",                                    "https://docs.krita.org/index.php?title=Grids_and_Guides"),
            ("Histogram docker",                                    "https://docs.krita.org/index.php?title=Histogram_docker"),
            ("Layers",                                              "https://docs.krita.org/index.php?title=Layers"),
            ("LUT Management",                                      "https://docs.krita.org/index.php?title=LUT_Management"),
            ("Onion Skin Docker",                                   "https://docs.krita.org/index.php?title=Onion_Skin_Docker"),
            ("Overview",                                            "https://docs.krita.org/index.php?title=Overview"),
            ("Palette",                                             "https://docs.krita.org/index.php?title=Palette"),
            ("Patterns",                                            "https://docs.krita.org/index.php?title=Patterns"),
            ("Reference Images",                                    "https://docs.krita.org/index.php?title=Reference_Images"),
            ("Shape Properties",                                    "https://docs.krita.org/index.php?title=Shape_Properties"),
            ("Small Color Selector",                                "https://docs.krita.org/index.php?title=Small_Color_Selector"),
            ("Snap Settings",                                       "https://docs.krita.org/index.php?title=Snap_Settings"),
            ("Specific Color Selector",                             "https://docs.krita.org/index.php?title=Specific_Color_Selector"),
            ("Task Sets",                                           "https://docs.krita.org/index.php?title=Task_Sets"),
            ("Timeline Docker",                                     "https://docs.krita.org/index.php?title=Timeline_Docker"),
            ("Undo History",                                        "https://docs.krita.org/index.php?title=Undo_History"),
        ("Filters",                                                 "https://docs.krita.org/index.php?title=Category:Filters"),
            ("Internal filters",                                    "https://docs.krita.org/index.php?title=Category:Internal_filters"),
                ("Adjust",                                          "https://docs.krita.org/index.php?title=Adjust"),
                ("Artistic",                                        "https://docs.krita.org/index.php?title=Artistic"),
                ("Blur",                                            "https://docs.krita.org/index.php?title=Blur"),
                ("Colors",                                          "https://docs.krita.org/index.php?title=Colors"),
                ("Edge Detection",                                  "https://docs.krita.org/index.php?title=Edge_Detection"),
                ("Emboss",                                          "https://docs.krita.org/index.php?title=Emboss"),
                ("Enhance",                                         "https://docs.krita.org/index.php?title=Enhance"),
                ("Map",                                             "https://docs.krita.org/index.php?title=Map"),
                ("Other filters",                                   "https://docs.krita.org/index.php?title=Other_filters"),
                ("Wavelet Decompose",                               "https://docs.krita.org/index.php?title=Wavelet_Decompose"),
        ("Layers and Masks",                                        "https://docs.krita.org/index.php?title=Category:Layers_and_Masks"),
            ("Clone Layers",                                        "https://docs.krita.org/index.php?title=Clone_Layers"),
            ("File Layers",                                         "https://docs.krita.org/index.php?title=File_Layers"),
            ("Fill Layers",                                         "https://docs.krita.org/index.php?title=Fill_Layers"),
            ("Filter Layers",                                       "https://docs.krita.org/index.php?title=Filter_Layers"),
            ("Filter Masks",                                        "https://docs.krita.org/index.php?title=Filter_Masks"),
            ("Group Layers",                                        "https://docs.krita.org/index.php?title=Group_Layers"),
            ("Layer Styles",                                        "https://docs.krita.org/index.php?title=Layer_Styles"),
            ("Local Selection Masks",                               "https://docs.krita.org/index.php?title=Local_Selection_Masks"),
            ("Paint Layers",                                        "https://docs.krita.org/index.php?title=Paint_Layers"),
            ("Transformation Masks",                                "https://docs.krita.org/index.php?title=Transformation_Masks"),
            ("Transparency Masks",                                  "https://docs.krita.org/index.php?title=Transparency_Masks"),
            ("Vector Layers",                                       "https://docs.krita.org/index.php?title=Vector_Layers"),
        ("Main Menu",                                               "https://docs.krita.org/index.php?title=Category:Main_Menu"),
            ("Edit Menu",                                           "https://docs.krita.org/index.php?title=Edit_Menu"),
            ("File Menu",                                           "https://docs.krita.org/index.php?title=File_Menu"),
            ("Help Menu",                                           "https://docs.krita.org/index.php?title=Help_Menu"),
            ("Image Menu",                                          "https://docs.krita.org/index.php?title=Image_Menu"),
            ("Layer Menu",                                          "https://docs.krita.org/index.php?title=Layer_Menu"),
            ("Select Menu",                                         "https://docs.krita.org/index.php?title=Select_Menu"),
            ("Settings Menu",                                       "https://docs.krita.org/index.php?title=Settings_Menu"),
            ("Tools Menu",                                          "https://docs.krita.org/index.php?title=Tools_Menu"),
            ("View Menu",                                           "https://docs.krita.org/index.php?title=View_Menu"),
            ("Window Menu",                                         "https://docs.krita.org/index.php?title=Window_Menu"),
        ("Preferences",                                             "https://docs.krita.org/index.php?title=Category:Preferences"),
            ("Author Settings",                                     "https://docs.krita.org/index.php?title=Author_Settings"),
            ("Canvas Input Settings",                               "https://docs.krita.org/index.php?title=Canvas_Input_Settings"),
            ("Canvas-only Settings",                                "https://docs.krita.org/index.php?title=Canvas-only_Settings"),
            ("Color Management Settings",                           "https://docs.krita.org/index.php?title=Color_Management_Settings"),
            ("Color Selector Settings",                             "https://docs.krita.org/index.php?title=Color_Selector_Settings"),
            ("Display Settings",                                    "https://docs.krita.org/index.php?title=Display_Settings"),
            ("General Settings",                                    "https://docs.krita.org/index.php?title=General_Settings"),
            ("Grid Settings",                                       "https://docs.krita.org/index.php?title=Grid_Settings"),
            ("Performance Settings",                                "https://docs.krita.org/index.php?title=Performance_Settings"),
            ("Shortcuts",                                           "https://docs.krita.org/index.php?title=Shortcuts"),
            ("Tablet Settings",                                     "https://docs.krita.org/index.php?title=Tablet_Settings"),
        ("Resource Management",                                     "https://docs.krita.org/index.php?title=Category:Resource_Management"),
            ("Managing Brush Presets",                              "https://docs.krita.org/index.php?title=Managing_Brush_Presets"),
            ("Managing Brush Tips",                                 "https://docs.krita.org/index.php?title=Managing_Brush_Tips"),
            ("Managing Gradients",                                  "https://docs.krita.org/index.php?title=Managing_Gradients"),
            ("Managing Patterns",                                   "https://docs.krita.org/index.php?title=Managing_Patterns"),
            ("Managing Workspaces",                                 "https://docs.krita.org/index.php?title=Managing_Workspaces"),
        ("Toolbox",                                                 "https://docs.krita.org/index.php?title=Category:Toolbox"),
            ("Assistant Tool",                                      "https://docs.krita.org/index.php?title=Assistant_Tool"),
            ("Bezier Curve Selection Tool",                         "https://docs.krita.org/index.php?title=Assistant_Tool"),
            ("Bezier Curve Tool",                                   "https://docs.krita.org/index.php?title=Bezier_Curve_Selection_Tool"),
            ("Calligraphy",                                         "https://docs.krita.org/index.php?title=Calligraphy"),
            ("Color Selector Tool",                                 "https://docs.krita.org/index.php?title=Color_Selector_Tool"),
            ("Contiguous Selection Tool",                           "https://docs.krita.org/index.php?title=Contiguous_Selection_Tool"),
            ("Crop Tool",                                           "https://docs.krita.org/index.php?title=Crop_Tool"),
            ("Dynamic Brush Tool",                                  "https://docs.krita.org/index.php?title=Dynamic_Brush_Tool"),
            ("Ellipse Tool",                                        "https://docs.krita.org/index.php?title=Ellipse_Tool"),
            ("Elliptical Selection Tool",                           "https://docs.krita.org/index.php?title=Elliptical_Selection_Tool"),
            ("Fill Tool",                                           "https://docs.krita.org/index.php?title=Fill_Tool"),
            ("Freehand Brush Tool",                                 "https://docs.krita.org/index.php?title=Freehand_Brush_Tool"),
            ("Freehand Path Tool",                                  "https://docs.krita.org/index.php?title=Freehand_Path_Tool"),
            ("Gradient Editing Tool",                               "https://docs.krita.org/index.php?title=Gradient_Editing_Tool"),
            ("Gradient Tool",                                       "https://docs.krita.org/index.php?title=Gradient_Tool"),
            ("Grid Tool",                                           "https://docs.krita.org/index.php?title=Grid_Tool"),
            ("Line Tool",                                           "https://docs.krita.org/index.php?title=Line_Tool"),
            ("Measure Tool",                                        "https://docs.krita.org/index.php?title=Measure_Tool"),
            ("Move Tool",                                           "https://docs.krita.org/index.php?title=Move_Tool"),
            ("Multibrush Tool",                                     "https://docs.krita.org/index.php?title=Multibrush_Tool"),
            ("Outline Selection Tool",                              "https://docs.krita.org/index.php?title=Outline_Selection_Tool"),
            ("Pan Tool",                                            "https://docs.krita.org/index.php?title=Pan_Tool"),
            ("Pattern Editing Tool",                                "https://docs.krita.org/index.php?title=Pattern_Editing_Tool"),
            ("Perspective Grid Tool",                               "https://docs.krita.org/index.php?title=Perspective_Grid_Tool"),
            ("Polygon Tool",                                        "https://docs.krita.org/index.php?title=Polygon_Tool"),
            ("Polygonal Selection Tool",                            "https://docs.krita.org/index.php?title=Polygonal_Selection_Tool"),
            ("Polyline Tool",                                       "https://docs.krita.org/index.php?title=Polyline_Tool"),
            ("Rectangle Tool",                                      "https://docs.krita.org/index.php?title=Rectangle_Tool"),
            ("Rectangular Selection Tool",                          "https://docs.krita.org/index.php?title=Rectangular_Selection_Tool"),
            ("Shape Handling Tool",                                 "https://docs.krita.org/index.php?title=Shape_Handling_Tool"),
            ("Similar Color Selection Tool",                        "https://docs.krita.org/index.php?title=Similar_Color_Selection_Tool"),
            ("Text Tool",                                           "https://docs.krita.org/index.php?title=Text_Tool"),
            ("Transform Tool",                                      "https://docs.krita.org/index.php?title=Transform_Tool"),
            ("Zoom Tool",                                           "https://docs.krita.org/index.php?title=Zoom_Tool"),
        ("Blending Modes",                                          "https://docs.krita.org/index.php?title=Blending_Modes"),
        ("Dr. Mingw debugger",                                      "https://docs.krita.org/index.php?title=Dr._Mingw_debugger"),
        ("Instant Preview",                                         "https://docs.krita.org/index.php?title=Instant_Preview"),
        ("Linux Command Line",                                      "https://docs.krita.org/index.php?title=Linux_Command_Line"),
        ("Maths input",                                             "https://docs.krita.org/index.php?title=Maths_input"),
        ("Render Animation",                                        "https://docs.krita.org/index.php?title=Render_Animation"),
        ("Stroke Selection",                                        "https://docs.krita.org/index.php?title=Stroke_Selection"),

    ("Tutorials",                                                   "https://docs.krita.org/index.php?title=Category:Tutorials"),
        ("Krita-Brush-tips",                                        "https://docs.krita.org/index.php?title=Category:Krita-Brush-tips"),
            ("Brush-tips:Animated Brush",                           "https://docs.krita.org/index.php?title=Brush-tips:Animated_Brush"),
            ("Brush-tips:Bokeh",                                    "https://docs.krita.org/index.php?title=Brush-tips:Bokeh"),
            ("Brush-tips:Caustics",                                 "https://docs.krita.org/index.php?title=Brush-tips:Caustics"),
            ("Brush-tips:Fur",                                      "https://docs.krita.org/index.php?title=Brush-tips:Fur"),
            ("Brush-tips:Hair",                                     "https://docs.krita.org/index.php?title=Brush-tips:Hair"),
            ("Brush-tips:Outline",                                  "https://docs.krita.org/index.php?title=Brush-tips:Outline"),
            ("Brush-tips:Rainbow Brush",                            "https://docs.krita.org/index.php?title=Brush-tips:Rainbow_Brush"),
            ("Brush-tips:Sculpt-paint-brush",                       "https://docs.krita.org/index.php?title=Brush-tips:Sculpt-paint-brush"),
        ("Clipping Masks and Alpha Inheritance",                    "https://docs.krita.org/index.php?title=Clipping_Masks_and_Alpha_Inheritance"),
        ("Common-workflows",                                        "https://docs.krita.org/index.php?title=Common-workflows"),
        ("External Training and Tutorials",                         "https://docs.krita.org/index.php?title=External_Training_and_Tutorials"),
        ("Flat Coloring",                                           "https://docs.krita.org/index.php?title=Flat_Coloring"),
        ("Inking",                                                  "https://docs.krita.org/index.php?title=Inking"),
        ("Making an Azalea with the transformation masks",          "https://docs.krita.org/index.php?title=Making_an_Azalea_with_the_transformation_masks"),
        ("Saving for the Web",                                      "https://docs.krita.org/index.php?title=Saving_for_the_Web"),

    ("Unstable Features",                                           "https://docs.krita.org/index.php?title=Category:Unstable_Features"),
        ("Audio for Animation",                                     "https://docs.krita.org/index.php?title=Audio_for_Animation"),
        ("Colorize Mask",                                           "https://docs.krita.org/index.php?title=Colorize_Mask"),
        ("GMIC filter plugin",                                      "https://docs.krita.org/index.php?title=GMIC_filter_plugin"),
        ("Python Plugin Manager",                                   "https://docs.krita.org/index.php?title=Python_Plugin_Manager"),
        ("Shape Selection Tool",                                    "https://docs.krita.org/index.php?title=Shape_Selection_Tool"),
        ("Smart Patch Tool",                                        "https://docs.krita.org/index.php?title=Smart_Patch_Tool"),
        ("Vector Graphics",                                         "https://docs.krita.org/index.php?title=Vector_Graphics"),

    ("Main page",                                                   "https://docs.krita.org/index.php?title=Main_Page"),

    ("KritaFAQ",                                                    "https://docs.krita.org/index.php?title=KritaFAQ"),

    ("Resources",                                                   "https://docs.krita.org/index.php?title=Resources"),

    # TODO: some missing pages not in the tree. See: https://docs.krita.org/Special:AllPages
    ])

# MediaWiki Actions: append these to the base url
ACTION_EDIT = '&action=edit'

ACTION_PRINT_AS_PDF = '&action=pdfbook&format=single'

PRINTABLE_VERSION = '&printable=yes'


def find_between(strng, first, last):
    try:
        start = strng.index(first) + len(first)
        end = strng.index(last, start)
        return strng[start:end]
    except ValueError:
        return ""


def download_mediawiki_pages():
    """
    Downloads the MediaWiki markup from the edit box on the edit page.
    """
    for pagename, url in list(PAGE_LINKS.items()):
        data = urllib2.urlopen(url + ACTION_EDIT)
        dataread = data.read()
        # print(dataread)  # Test to make sure we have the mediawiki box data.
        mediawiki_markup = find_between(strng=dataread, first='name="wpTextbox1">', last='</textarea>')
        if mediawiki_markup:
            pagenamedotmediawiki = pagename.replace('*', '').replace(' ', '_') + '.mediawiki'
            print("Writing %s" % pagenamedotmediawiki)
            with open(pagenamedotmediawiki, 'w') as f:
                f.write(mediawiki_markup)


def download_mediawiki_pdfs():
    """
    Downloads the pdfs for the "print as pdf" for the pages.
    """
    for pagename, url in list(PAGE_LINKS.items()):
        data = urllib2.urlopen(url + ACTION_PRINT_AS_PDF)
        dataread = data.read()
        # print(dataread)  # Test to make sure we have pdf data.
        if dataread:
            pagenamedotpdf = pagename.replace('*', '') + '.pdf'
            print("Writing %s" % pagenamedotpdf)
            with open(pagenamedotpdf, 'wb') as f:
                f.write(dataread)


def mediawiki_to_rst_with_pandoc(pandocExe):
    cwd = os.path.dirname(__file__)
    for filename in os.listdir(cwd):
        if filename.endswith('.mediawiki'):
            input = cwd + os.sep + filename
            output = cwd + os.sep + filename.replace('.mediawiki', '.rst')
            args = "%s -f mediawiki -t rst -o %s %s" % (pandocExe, output, input)
            print("Converting %s to %s" % (input, output))
            subprocess.Popen(args)
            # break  # only do one file to test first.



if __name__ == '__main__':
    print('Python %s' % sys.version)

    # print("Starting Downloading MediaWiki content...")
    # download_mediawiki_pages()

    # print("Starting Converting mediawiki to rst with pandoc...")
    # pandocExe = r"C:\Users\username\AppData\Local\Pandoc\pandoc.exe"
    # mediawiki_to_rst_with_pandoc(pandocExe)

    print("Starting Downloading PDF's")
    download_mediawiki_pdfs()

