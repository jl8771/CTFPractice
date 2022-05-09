### The name of the challenge combined with the hint from the challenge
>The flag is somewhere on this web application not necessarily on the website.
### leads me to believe the flag may be hidden in the robots.txt file. Appending a `/robots.txt` to the end of the URL leads to a webpage that says
___
<p>
User-agent *
</br>
Disallow: /cgi-bin/
</br>
Think you have seen your flag or want to keep looking.
</br>
</br>
ZmxhZzEudHh0;anMvbXlmaW
</br>
anMvbXlmaWxlLnR4dA==
</br>
svssshjweuiwl;oiho.bsvdaslejg
</br>
Disallow: /wp-admin/
</p>

___
### Using `base64` to decode the string as a whole leads to an invalid input. However, splitting it up into three strings as displayed allows for a `flag1.txt` and a `js/myfile.txt` to be seen. Appending the `/flag1.txt` leads to a 404 but appending the `/js/myfile.txt` leads to the flag.