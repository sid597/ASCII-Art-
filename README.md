# ASCII-Art-
Turn images to Ascii Art  ;) 

![alt text](https://octodex.github.com/images/steroidtocat.png)
![alt text](https://raw.githubusercontent.com/sid597/ASCII-Art-/master/steroidCat.png)






How you can use this to get your fav characte in Ascii Art ? 
- Clone the repo
- In terminal run python ascii.py  /path-to-file.png 

You can provide any format of image you would like, I did tried this with png,jpg,jpeg formats

There are 5 simple steps to this project :
1) Choose an image ( In my project you can pass the path to your image )
2) Read your image and print its height and width in pixels
3) Load your image’s pixel data into a 2-dimensional array
4) Convert brightness numbers to ASCII characters
5) Print your ASCII art! 

Some Issues one might face after following all the above steps :
  1) Image might look squashed : This is due to characters in terminal are rectangle one of the         ways to fix this is print each character in row 3 times
  2) Matrix is too large for screen : To tackle this one can resize the terminal zoom and can           also resize the image. I have a big monitor so I have set resize width to 440 and the           height is set automatically ( keeping aspect ratio of image same ). I use terminator             with infinte scroll so I can scroll more if image gets out of the terminal. 
  
  
