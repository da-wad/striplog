# -*- coding: utf 8 -*-
"""
Defines a suite a tests for images run with:

    py.test --mpl

To generate new test images, see the instructions in
striplog/run_tests.py

https://pypi.python.org/pypi/pytest-mpl/0.3
"""
import random

import matplotlib.pyplot as plt
import pytest

from striplog import Striplog
from striplog import Legend, Component, Decor

params = {'tolerance': 20,
          'savefig_kwargs': {'dpi': 100},
          }


@pytest.mark.mpl_image_compare(**params)
def test_striplog_plot():
    """
    Tests mpl image of striplog.
    """
    legend = Legend.builtin('NSDOE')

    imgfile = "tutorial/M-MG-70_14.3_135.9.png"

    striplog = Striplog.from_image(imgfile, 14.3, 135.9, legend=legend)

    fig = striplog.thickest(n=5).plot(legend=legend,
                                      ladder=False,
                                      return_fig=True)
    return fig


@pytest.mark.mpl_image_compare(**params)
def test_striplog_ladder_plot():
    """
    Tests mpl image of striplog with the ladder option.
    """
    legend = Legend.builtin('NSDOE')

    imgfile = "tutorial/M-MG-70_14.3_135.9.png"

    striplog = Striplog.from_image(imgfile, 14.3, 135.9, legend=legend)

    fig = striplog.thickest(n=5).plot(legend=legend,
                                      ladder=True,
                                      return_fig=True)
    return fig


@pytest.mark.mpl_image_compare(**params)
def test_striplog_colour_plot():
    """
    Tests mpl image of striplog with the ladder option.
    """
    legend = Legend.builtin('NSDOE')

    imgfile = "tutorial/M-MG-70_14.3_135.9.png"

    striplog = Striplog.from_image(imgfile, 14.3, 135.9, legend=legend)

    for iv in striplog:
        iv.data['porosity'] = iv.top.z/100

    fig = striplog.plot(colour='porosity', aspect=3, return_fig=True)

    return fig


@pytest.mark.mpl_image_compare(**params)
def test_striplog_point_plot():
    """
    Tests mpl image of striplog with the points option.
    """
    legend = Legend.builtin('NSDOE')

    imgfile = "tutorial/M-MG-70_14.3_135.9.png"

    striplog = Striplog.from_image(imgfile, 14.3, 135.9, legend=legend)

    for iv in striplog:
        iv.data['porosity'] = iv.top.z/100

    fig = striplog.plot(style='points',
                        field='porosity',
                        aspect=3,
                        return_fig=True)

    return fig


@pytest.mark.mpl_image_compare(**params)
def test_striplog_top_plot():
    """
    Tests mpl image of striplog with the tops option.
    """
    tops_csv = """top, Comp formation
                   25, Escanilla Fm.
                   35, San Vicente Fm.
                   20, Sobrarbe Fm.
                   50, Cretaceous"""

    tops = Striplog.from_csv(text=tops_csv)

    fig = tops.plot(style='tops',
                    field='formation',
                    aspect=1.5,
                    return_fig=True)

    return fig


@pytest.mark.mpl_image_compare(**params)
def test_decor_plot():
    """
    Tests mpl image of decor.
    """
    r = {'colour': 'grey',
         'grainsize': 'vf-f',
         'lithology': 'sand'}

    rock = Component(r)

    d = {'color': '#86F0B6',
         'component': rock,
         'width': 3}

    decor = Decor(d)

    fig = plt.figure(figsize=(4, 1))
    fig = decor.plot(fmt="{lithology!t} {colour} {grainsize}", fig=fig)
    return fig


@pytest.mark.mpl_image_compare(**params)
def test_pattern_fills():
    """
    Tests mpl image of decors with pattern fills.
    """
    hatches = "pctLbs!=v^"
    decors = [Decor({'component': Component({'hatch': h}),
                     'hatch': h,
                     'colour': '#eeeeee'})
              for h in hatches]

    fig = plt.figure(figsize=(1, 12))
    for i, d in enumerate(decors):
        ax = fig.add_subplot(len(decors), 1, i+1)
        ax = d.plot(ax=ax, fmt='')
    return fig
