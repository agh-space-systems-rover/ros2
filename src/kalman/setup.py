from setuptools import find_packages, setup
import glob
import os

package_name = "kalman"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (
            os.path.join("share", package_name, "launch"),
            glob.glob(os.path.join("launch", "*launch.[pxy][yma]*")),
        ),
        (
            "share/" + package_name + "/config",
            glob.glob(os.path.join("config", "*")),
        ),
    ],
    zip_safe=True,
    maintainer="rayferric",
    maintainer_email="63957587+rayferric@users.noreply.github.com",
    description="TODO: Package description",
    license="TODO: License declaration",
    entry_points={
        "console_scripts": [],
    },
)
