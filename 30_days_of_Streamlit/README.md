# Streamlit Challenge - 30 Days of Streamlit

[Streamlit](https://streamlit.io/) is a Python library that allows the creation of interactive, data-driven web applications in Python.

## Day 1

```powershell

# install the streamlit library
pip install streamlit

# To launch the Streamlit demo app on localhost:8501
streamlit hello

```

## Day 2

```powershell

# Run the first streamlit app
streamlit run 02_app.py

```

## Day 3

`st.button` allows the display of a button widget.

What are we Building?

A simple app that performs conditionally prints out alternative messages depending on whether the button was pressed or not.

Flow of the app:

- By default, the app prints "Goodbye"
- Upon clicking on the button, the app displays the alternative message "Why hello there"


```powershell

streamlit run 03_app.py

```

## Day 4


## Day 5

`st.write` allows writing text and arguments to the Streamlit app.


```powershell

streamlit run 05_app.py

```

## Day 6
Uploading your Streamlit app to GitHub

## Day 7
Deploying your Streamlit app with Streamlit Community Cloud (a hosting service for easily deploying Streamlit apps).

## Day 8

`st.slider` allows the display of a slider input widget.
The following data types are supported: int, float, date, time, and datetime.

What we're building?
A simple app that shows the various ways on how to accept user input by adjusting the slider widget.

Flow of the app:

- User selects value by adjusting the slider widget
- App prints out the selected value

```powershell

streamlit run 08_app.py

```
## Day 9

`st.line_chart` displays a line chart.

What we're building?
A simple app for displaying a line chart.

Flow of the app:

- Create a Pandas DataFrame from numbers randomly generated via NumPy.
- Create and display the line chart via st.line_chart() command.

```powershell

streamlit run 09_app.py


```

## Day 10

`st.selectbox` allows the display of a select widget.
What we're building?
A simple app that asks the user what their favorite color is.

Flow of the app:

- User selects a color
- App prints out the selected color

```powershell

streamlit run 10_app.py

```

## Day 11

`st.multiselect` displays a multiselect widget.

```powershell

streamlit run 11_app.py

```

## Day 12

`st.checkbox` displays a checkbox widget.

```powershell

streamlit run 12_app.py

```

## Day 13

Spin up a cloud development environment with Gitpod

Other options:
- GitHub Codespaces
- Replit
- Cloud9

## Day 14

Streamlit Components

Components are third-party Python modules that extend whats possible with Streamlit.

How to use?
Streamlit components are just a pip-install away.

In this tutorial, let's get you started in using the `streamlit_pandas_profiling` component.

```powershell
# Install the streamlit_pandas_profiling component
pip install streamlit_pandas_profiling

# Run the app
streamlit run 14_app.py

```
## Day 15

`st.latex` displays mathematical expressions formatted as LaTeX.

```powershell

streamlit run 15_app.py

```

## Day 16

Customizing the theme of Streamlit apps
We can customize the theme by adjusting parameters in config.toml, which is a configuration file stored in the same folder as the app in the .streamlit folder.

What we're building?
A simple app that shows the result of our theme customization. This is made possible by customizing the HTML HEX code inside the .streamlit/config.toml file.

```powershell   

streamlit run 16_app.py

```

## Day 17

`st.secrets` allows you to store confidential information such as API keys, database passwords or other credentials.

It should be noted that, secrets can be stored in Streamlit Community Cloud as shown in the screenshots shown below.

If working locally, they can be stored in .streamlit/secrets.toml, but make sure to avoid uploading this to a GitHub repo when deploying the app.

```powershell

streamlit run 17_app.py

```

## Day 18

`st.file_uploader` displays a file uploader widget.

By default, uploaded files are limited to 200MB. You can configure this using the server.maxUploadSize config option

```powershell

streamlit run 18_app.py

```

## Day 19

How to layout your Streamlit app
In this tutorial, we're going to use the following commands to layout our Streamlit app:

- st.set_page_config(layout="wide") - Displays the contents of the app in wide mode (otherwise by default, the contents are encapsulated in a fixed width box.
- st.sidebar - Places the widgets or text/image displays in the sidebar.
- st.expander - Places text/image displays inside a collapsible container box.
- st.columns - Creates a tabular space (or column) within which contents can be placed inside.

```powershell

streamlit run 19_app.py

```

## Day 20

Tech Twitter Space on What is Streamlit?

## Day 21

`st.progress` displays a progress bar that updates graphically as the iteration progresses.

```powershell
streamlit run 21_app.py

```

## Day 22

`st.form` creates a form that batches elements together with a "Submit" button.

Typically, whenever a user interacts with a widget, the Streamlit app is rerun.

A form is a container that visually groups other elements and widgets together, and contains a Submit button. Herein, a user can interacts with one or more widgets for as many times as they like without causing a rerun. Finally, when the form's Submit button is pressed, all widget values inside the form will be sent to Streamlit in a single batch.

To add elements to a form object, you can use the with notation (preferred) or you could use it as an object notation by just calling methods directly on the form (by first assigning it to a variable and subsequently applying Streamlit methods on it). See in the example app.

Forms have a few constraints:

- Every form must contain a st.form_submit_button.
- st.button and st.download_button cannot be added to a form.
- Forms can appear anywhere in your app (sidebar, columns, etc), but they cannot be embedded inside other forms.

```powershell

streamlit run 22_app.py

```

## Day 23

`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.

```powershell
streamlit run 23_app.py

```
## Day 24

st.cache allows you to optimize the performance of your Streamlit app.

Streamlit provides a caching mechanism that allows your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations. This is done with the @st.cache decorator.

When you mark a function with the @st.cache decorator, it tells Streamlit that whenever the function is called it needs to check a few things:

- The input parameters that you called the function with
- The value of any external variable used in the function
- The body of the function
- The body of any function used inside the cached function

If this is the first time Streamlit has seen these four components with these exact values and in this exact combination and order, it runs the function and stores the result in a local cache. Then, next time the cached function is called, if none of these components changed, Streamlit will just skip executing the function altogether and, instead, return the output previously stored in the cache.

The way Streamlit keeps track of changes in these components is through hashing. Think of the cache as an in-memory key-value store, where the key is a hash of all of the above and the value is the actual output object passed by reference.

Finally, @st.cache supports arguments to configure the cache's behavior. You can find more information on those in our API reference.

How to use?
You can simply add st.cache decorator on the preceding line of a custom function that you define in your Streamlit app. See the example below.

```powershell	
streamlit run 24_app.py

```

## Day 25

We define access to a Streamlit app in a browser tab as a session. For each browser tab that connects to the Streamlit server, a new session is created. Streamlit reruns your script from top to bottom every time you interact with your app. Each reruns takes place in a blank slate: no variables are shared between runs.

Session State is a way to share variables between reruns, for each user session. In addition to the ability to store and persist state, Streamlit also exposes the ability to manipulate state using Callbacks.

In this tutorial, we will illustrate the usage of Session State and Callbacks as we build a weight conversion app.

`st.session_state` allows the implementation of session state in a Streamlit app.

```powershell

streamlit run 25_app.py

```

## Day 26

How to use API by building the Bored API app
The Bored API app suggests fun things for you to do when you are bored!

Technically, it also demonstrates the usage of APIs from within a Streamlit app.

```powershell

streamlit run 26_app.py

```

## Day 27

What are we building?
The goal of today's challenge is to create a dashboard composed of three Material UI cards:

A first card with a Monaco code editor to input some data ;
A second card to display that data in a Nivo Bump chart ;
A third card to show a YouTube video URL defined with a st.text_input.
You can use data generated from Nivo Bump demo there, in 'data' tab: https://nivo.rocks/bump/.

```powershell

streamlit run 27_app.py

```


## Day 28

`streamlit-shap` is a Streamlit component that provides a wrapper to display SHAP plots in Streamlit.

```powershell

streamlit run 28_app.py

```


## Day 29

How to make a zero-shot learning text classifier using Hugging Face and Streamlit

```powershell 

streamlit run 29_app.py

```

## Day 30

```powershell

streamlit run 30_app.py

```

