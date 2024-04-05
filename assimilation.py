#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from solvers import RK4_step, integrate_step


class Assimilation:
        


class Observation:
    def __init__(self, R, random_generator=np.random.default_rng):
        """
        Keyword Arguments:
        R -- Covariance matrix of the observations
        """
        self.R = R
        self.rng = random_generator

    def sample_observation_error(self, size):
        return self.rng.multivariate_normal(np.zeros(len(self.R)), cov=self.R)
