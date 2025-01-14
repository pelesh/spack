# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOptax(PythonPackage):
    """A gradient processing and optimisation library in JAX."""

    homepage = "https://github.com/deepmind/optax"
    pypi = "optax/optax-0.1.7.tar.gz"

    license("Apache-2.0")

    version("0.1.7", sha256="6a5a848bc5e55e619b187c749fdddc4a5443ea14be85cc769f995779865c110d")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-flit-core@3.2:3", type="build")
    depends_on("py-absl-py@0.7.1:", type=("build", "run"))
    depends_on("py-chex@0.1.5:", type=("build", "run"))
    depends_on("py-jax@0.1.55:", type=("build", "run"))
    depends_on("py-jaxlib@0.1.37:", type=("build", "run"))
    depends_on("py-numpy@1.18.0:", type=("build", "run"))
