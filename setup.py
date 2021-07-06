from setuptools import setup

setup(
    name='DeepLearningPractice',
    version='0.1',
    description='Deep learning trial package',
    py_modules=["train", "utils"],
    install_requires=['torch', 'torchvision', 'numpy', 'hydra'],
    # entry_points = {
    #     '...': [
    #         'entry point function' = ...
    #     ]
    # },
)

