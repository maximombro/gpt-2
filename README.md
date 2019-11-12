# GPT-2M
GPT-2M ecompasses an effort to turn OpenAI's GPT-2 developer example into something that can be used with more ease and further extend it's uses towards creative and artisitc means.

## Project Goals
- [ ] Text based menu for controlling GPT-2M
- [ ] Support for importing starting samples from a file
- [ ] Support for exporting generated text to a file
- [ ] Introduce support for Tensor 2.*
- [ ] Provide a more user friendly installation process

## Setting Up GPT-2M
Instructions adapted and corrected from a Medium article found [here](https://medium.com/@ngwaifoong92/beginners-guide-to-retrain-gpt-2-117m-to-generate-custom-text-content-8bb5363d8b7f).
See [Developers.md](./DEVELOPERS.md) for more information.
1. Download this repo.
1. Ensure you have Python 3.7 64bit installed.
	* On Windows, it's helpful to check `Add Python (VERSION) to PATH`.
	* You should also check to see if your system is linked to use `python` or `python3` in the command line to use Python 3.
	* The version of each command can be checked with `python -V` or `python3 -V`.
1. Open a command window in the GPT-2M Directory.
1. Run `$ pip install -r .\requirements.txt` ensuring that `pip` relates to the one installed for Python 3.
	* An error can occur stating `Microsoft Visual C++ 14.0 is required`.
		1. Scroll down to `Build Tools for Visual Studio 2019` [here](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019).
		1. Download and run the installer.
		1. Check off `C++ build tools` under the `Workloads` top header.
		1. Click `Install` in the bottom right.
		1. Restart the computer when prompted and try this step's pip command again.
	* You may also need to run `$ pip install --upgrade setuptools` after installing the C++ Build Tools.
1. Run `$ pip install tensorflow-gpu==1.15.0` to install the 1.15.0 (not the most recent) TensorFlow enviroment to your Python 3.7.* installation with GPU priority.
	* Remove the `-gpu` text to install without GPU priority.
1. Run `$ python download_model.py 774M` to download the GPT-2 data model.
	* You should replace `python` with `python3` in all following inputs if that is how your `PATHS` are setup.
	* You can also replace `774M` with `335M` or `124M` if you want a smaller model download file size but reduced accuracy.
1. Run `$ python \src\interactive_conditional_samples.py --model_name 774M --top_k 40 --tempurature 0.8` to test the output.
	* You will be prompted (after some warnings) with `Model prompt >>>`. Enter whatever text you want the system to finish here.
		* After hitting `Enter` the program will run for a while and eventually return a text sample to the console.
	* Hit `CTRL+C` to exit the execution.

## Attributions
* Code and models from the paper ["Language Models are Unsupervised Multitask Learners"](https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf).
* GPT-2 was originally written under [OpenAI](https://github.com/openai/gpt-2).
* Released by OpenAI under the [MIT License](./LICENSE).
