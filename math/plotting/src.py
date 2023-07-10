#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


def line():
    y = np.arange(0, 11) ** 3
    plt.plot(y, color="red")
    plt.xlim(0, 10)


def scatter(text_kwargs=None):
    text_kwargs = text_kwargs or {}
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180

    plt.scatter(x, y, c="magenta")
    plt.xlabel("Height (in)", **text_kwargs)
    plt.ylabel("Weight (lbs)", **text_kwargs)
    plt.title("Men's Height vs Weight", **text_kwargs)


def log_scale(text_kwargs=None):
    text_kwargs = text_kwargs or {}
    x = np.arange(0, 28651, 5730)
    r = np.log(0.5)
    t = 5730
    y = np.exp((r / t) * x)

    plt.plot(x, y)
    plt.yscale("log")
    plt.xlim(0, 28650)
    plt.xlabel("Time (years)", **text_kwargs)
    plt.ylabel("Fraction Remaining", **text_kwargs)
    plt.title("Exponential Decay of C-14", **text_kwargs)


def two(text_kwargs=None):
    text_kwargs = text_kwargs or {}
    x = np.arange(0, 21000, 1000)
    r = np.log(0.5)
    t1 = 5730
    t2 = 1600
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)

    plt.plot(x, y1, "r--", label="C-14")
    plt.plot(x, y2, "g-", label="Ra-226")
    plt.xlim(0, 20000)
    plt.ylim(0, 1)
    plt.xlabel("Time (years)", **text_kwargs)
    plt.ylabel("Fraction Remaining", **text_kwargs)
    plt.title("Exponential Decay of Radioactive Elements", **text_kwargs)
    plt.legend(loc="upper right", **text_kwargs)


def frequency(text_kwargs=None):
    text_kwargs = text_kwargs or {}
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor="black")
    plt.xlabel("Grades", **text_kwargs)
    plt.ylabel("Number of Students", **text_kwargs)
    plt.title("Project A", **text_kwargs)
    plt.xlim(0, 100)
    plt.ylim(0, 30)


def all_in_one():
    text_kwargs = {"fontsize": "x-small"}
    plt.suptitle("All in One")
    plt.subplot(321)
    line()
    plt.subplot(322)
    scatter(text_kwargs)
    plt.subplot(323)
    log_scale(text_kwargs)
    plt.subplot(324)
    two(text_kwargs)
    plt.subplot(313)
    frequency(text_kwargs)
    plt.tight_layout()
    plt.show()
