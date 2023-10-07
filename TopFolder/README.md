# Folder Structure

This is the top level of the presentation. Place all your elements here

## Available Elements

### Folder
A folder will be seen as a new Section and can have its own subsections in it. 

The maximum depth of a folder is 2.

#### Naming
Folders need to be named like this:
```
{number}--{Sectionname}
```
The number specifies the order of the folder

### Picture
A picture will be put on a slide alone or with something else.

#### Naming
Pictures need to be named like this:
```
{number}--{slideName}--{minsize}--{caption}.{fileending}
```

- `number` specifies the order of the elements. If there are other numbered elements (like folders or text) they will be also counted.
- `slideName` name of the slide
- `minsize` specify the size of the image on the slide. If possible a bigger size will be taken. Available sizes are:
    - 1 (full width)
    - 2 (half width)
    - 3 (1/3 width)
- `caption` specify the caption of the image. No caption will be produced if left empty
- `fileending` supported fileendings are:
    - .png
    - .jpg

### TeX
A TeX code snippet. Can be on a slide alone or with something else.

NOTE: No preamble or anything needed

#### Naming
TeX snippets need to be named like this:
```
{number}--{slideName}.tex
```

- `number` specifies the order of the elements. If there are other numbered elements (like folders or pictures) they will be also counted.
- `slideName` name of the slide
