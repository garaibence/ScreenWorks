-- +--------------------------------------------------------+
-- | GitHub repo: https://github.com/garaibence/ScreenWorks |
-- +--------------------------------------------------------+

Width   = 80
Height  = 45
Color  = true
Start   = 35
End     = 126

divider = 255 / (End - Start)
mult = 0
switch = true
data = ""

for i=1, Width*Height*3, 1 do
	data = data .. " "
end

function onTick()
    async.httpGet(8080, "/data?start=" .. Start .. "&end=" .. End .. "&w=" .. Width .. "&h=" .. Height .. "&c=" .. tostring(Color))
	output.setNumber(1, tonumber(string.sub(data, -6)))
end

function httpReply(port, request_body, response_body)
	data = response_body
end

function onDraw()
	if switch then
		if screen.getWidth()/screen.getHeight() < Width / Height then
			mult = screen.getWidth() / Width
		else
			mult = screen.getHeight() / Height
		end
		switch = false
	end
	for y=0, Height-1, 1 do
    	for x=0, Width-1, 1 do
			if Color then
    			r = (Width*y+x)*3+1
    			g = (Width*y+x)*3+2
    			b = (Width*y+x)*3+3
			else
				r = Width*y+x+1
				g = Width*y+x+1
				b = Width*y+x+1
			end
    		screen.setColor((data:byte(r)-Start)*divider,(data:byte(g)-Start)*divider,(data:byte(b)-Start)*divider)
			screen.drawRectF(screen.getWidth()/2-mult*Width/2+mult*x,screen.getHeight()/2-mult*Height/2+mult*y,mult,mult)
    	end
    end

end