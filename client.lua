-- +--------------------------------------------------------+
-- | GitHub repo: https://github.com/garaibence/ScreenWorks |
-- +--------------------------------------------------------+

width   = 80
height  = 45
colour  = true

Start   = 35
End     = 126
Divider = 255 / (End - Start)

mult = 0
switch = true
data = ""

for i=1, width*height*3, 1 do
	data = data .. " "
end

function onTick()
    async.httpGet(8080, "/data?w=" .. width .. "&h=" .. height .. "&c=" .. tostring(colour))
end

function httpReply(port, request_body, response_body)
	data = response_body
end

function onDraw()
	if switch then
		if screen.getWidth()/screen.getHeight() < width / height then
			mult = screen.getWidth() / width
		else
			mult = screen.getHeight() / height
		end
		switch = false
	end
	for y=0, height-1, 1 do
    	for x=0, width-1, 1 do
			if colour then
    			r = (width*y+x)*3+1
    			g = (width*y+x)*3+2
    			b = (width*y+x)*3+3
			else
				r = width*y+x+1
				g = width*y+x+1
				b = width*y+x+1
			end
    		screen.setColor((data:byte(r)-Start)*Divider, (data:byte(g)-Start)*Divider, (data:byte(b)-Start)*Divider)
			screen.drawRectF(screen.getWidth()/2-mult*width/2+mult*x,screen.getHeight()/2-mult*height/2+mult*y,mult,mult)
    	end
    end

end