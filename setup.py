from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-tesseract-scanner",
    version="0.1.0",
    author="Pham Xuan Tien",
    author_email="phamxtien@gmail.com",
    description="OCR Scanner use tesseract",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.9",
    install_requires=["streamlit>=1.15"],
    url="https://github.com/phamxtien/streamlit_tesseract_scanner",
)
