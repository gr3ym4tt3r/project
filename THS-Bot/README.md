# Poster Chatter Thingy

    [14|Aug 09:47 PM]:	ch3rn0byl minion: New post in response to DefCon 24 Short Stories! Doc, try to refrain from making more 50 shades of grey stories hehe.. Click here to view: http://forum.top-hat-sec.com/index.php?topic=5642.msg45904#msg45904
    
Here's a script that will watch Top Hat for any new posts. Once there is a post and it sees it, it will grab what it needs and post it in the chatbox.  
Way this was achieved was I noticed that the rss page...nothing changes so I hashed it with MD5 and conduct the check like that. If there is a difference, obviously something changed and it grabs the post and posts it in chat. 
It also texts me with the new response that way I can get it to my phone. Mainly to use up my twilio credits...   

# Just thoughts on what next to add

Eventually, I will add a function to post on a new member's introduction and welcome them because I'm too lazy to say hi myself. I also suck at hi's.  
Thats it for now

# Issues Fixed

One of the issues I was having was my bot was including the html tags when someone would posts links or smiley faces or whatever. 
For example: 
  
    ch3rn0byl minion: New post in response to Board of Shame! Board of shame. Tsk tsk&nbsp; <img src="http://forum.top-hat-sec.com/Smileys/default/cool.gif" alt="8&#41;" title="Cool" class="smiley" /> hehe <img src="http://forum.top-hat-sec.com/Smileys/default/smiley.gif" alt="&#58;&#41;" title="Smiley" class="smiley" />.. Click here to view   
    
That's obviously a no go because it looks ugly as hell. Finally figured out how to fix it and hopefully its done...  

    ch3rn0byl minion: New post in response to Board of Shame! Board of shame. Tsk tsk hehe .. Click here to view
