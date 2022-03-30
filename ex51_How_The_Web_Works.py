# How the web works

# A. Your browser
# B. Network interface
# C. The internet
# D. My server
# E. web app's index.GET

# 1. you type in the url into your browser, and it sends the request line between
# A and B to your computer's nertwork interface.

# 2. Your request goes out over the internet between B and C and then to the remote
# computer on line C, where my server accepts the request.

# 3. Once my computer accepts it, my web application gets between D and E, and my
# Python code runs the index.GET handler.

# 4. The response comes out of my Python server when I return it, and it goes
# back to your browser between D and E again.

# 5. The server running this site takes the response off between D and E, then
# sends it back over the internet between C and D.

# 6. The response from the server then comes off the internet between B and C,
# and your computer's network interface hands it to your browser betweeen A and B.

# 7. Finally, your browser then displays the response.

# In this description there are a few terms you should know so that you have a
# common vocabulary to work with when talking about your web application:

# Browser: it's job is to take addresses you type into the URL bar then use that
# info to make requests to the server at that address.

# Address: this is normally a URL (Uniform Resource Locator) and indicates where a
# browser should go. The first part, 'http' indicates a protocol you want to use, in
# this case "Hyper text Transport Protocol". You can also try ftp://ibiblio.org to see
# how "File transport Protocol" works.  The http://test.com/ part is the "hostname",
# a human readable address you can remember and which maps to a number called an IP address,
# similar to a telephone number for a computer on the internet. Finally, URLs have a trailing
# path like the /book/ part of http://test.com/book/, which indicates a file or some resource
# on the server to retreieve with a request. There are many other parts, but those are the main
# ones.

# Connection: When your browser knows what protocol you want to use (http), what server you
# want to talk to, and what resourvce on that server to get it, it must make a connection.
# The browser asks your OS to open a "port" to the computer (80 usually). When it works,
# the OS hands back to your program something that works like a file, but is actually sending
# and receiving bytes over the network wires between your pc and others at the url.

# Request: Your browser is connected using the address you gave. Now it needs to ask for
# the resource it wants on the remote server

# Server:

# Response:
