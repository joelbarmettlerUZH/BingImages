# Bing Images - unofficial API
BingImages is a python packages which lets you easily search for images online using the bing images search engine. BingImages offers you the following cool features:

- Search for images like you would using any search engine
- Filter your search results with detailed filters
- Download all images to your local disk

## How to get it

To get BingImages, you can simply use pip:

```sh
pip install BingImages
```

Or you can clone [this](https://github.com/joelbarmettlerUZH/BingImages) repository and copy-paste all files contained in the *BingImages* folder into your project directory.

## Usage

BingImages is deadly simple. Let's have a look at the most important features:

### Simple search

To quickly search for images regarding one specific topic, just write the following line of code:

```python
from BingImages import BingImages

musk = BingImages("Elon Musk").get()
```

The musk variable now contains a set of 35 links that fit the serachterm "Elon Musk" best. 

### Filter results

You can do more advanced searches by filtering your search-request:

#### Number of Images
Only returns the first X images from the search result.

```python
musk = BingImages("Elon Musk", count=5).get()
```

Possible attributes: **Any number you'd like**.

#### Image Color
Only returns images whose primary color is the specified color. 

```python
musk = BingImages("Elon Musk", color="red").get()
```

Possible attributes: **yellow, orange, green, red, teal, black, white, grey, blue, purple, pink, brown, gray**.

#### Image Size
Only returns images of a certain Size

```python
musk = BingImages("Elon Musk", size="small").get()
```

Possible attributes: **small, medium, large, wallpaper**.

#### Image Type
Only returns images of a certain Type

```python
musk = BingImages("Elon Musk", type="photo").get()
```

Possible attributes: **photo, clipart, linedrawing, animatedgif, transparent**.

#### Image Layout
Only returns images of a certain Layout

```python
musk = BingImages("Elon Musk", layout="square").get()
```

Possible attributes: **square, wide, tall**.

#### Image Person
Only returns images of a certain Layout

```python
musk = BingImages("Elon Musk", person="portrait").get()
```

Possible attributes: **face, portrait**.

#### Image Age
Only returns images that were taken during in the specified timeperiod.

```python
musk = BingImages("Elon Musk", age="day").get()
```

Possible attributes: **day, week, month, year**.

#### Image License
Only returns images that fall under the specified license.

```python
musk = BingImages("Elon Musk", licensetype="publicDomain").get()
```

Possible attributes: **creativeCommons, publicDomain**.

License
----

MIT License

Copyright (c) 2018 Joel Barmettler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


By the way, I am an [AI Engineer from Zurich](https://joelbarmettler.xyz/) and do [AI research](https://joelbarmettler.xyz/research/), [AI Keynote Speaker](https://joelbarmettler.xyz/auftritte/) and [AI Webinars](https://joelbarmettler.xyz/auftritte/webinar-2024-rewind-2025-ausblick/) in Zurich, Switzerland! I also have an [AI Podcast in swiss german](https://joelbarmettler.xyz/podcast/)!
