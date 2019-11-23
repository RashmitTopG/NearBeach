function render_bug_client_bugs(e,t){var n={};for(row in e){var i=e[row].bug_status;for(status in i)n[status]=status}n=Object.keys(n).sort(function(e,t){return n[e]-n[t]}),console.log("Unique bug status: ",n);var o=[];for(row in e){i=e[row].bug_status;var r={bug_client_name:row};n.forEach(function(e){null==i[e]?r[e]=0:r[e]=i[e]}),o.push(r)}var s=40,a=100,l=80,c=50,d=960-c-a,u=500-s-l;console.log("Converted Data: ",o);var f=d3.scaleBand().rangeRound([0,d],.15).paddingInner(.2).paddingOuter(.2),h=d3.scaleLinear().range([u,0]),m=d3.scaleOrdinal(d3.schemePastel2),p=d3.axisBottom().scale(f),_=d3.axisLeft().scale(h).ticks(10),g=document.getElementById(t);g.innerHTML="";var v=d3.select(g).append("svg").attr("width",d+c+a).attr("height",u+s+l).attr("data-graph",g.id).attr("class","graph_body").append("g").attr("transform","translate("+c+","+s+")");m.domain(d3.keys(o[0]).filter(function(e){return"bug_client_name"!==e})),o.forEach(function(e){var t=0;e.operation=m.domain().map(function(n){return{name:n,y0:t,y1:t+=+e[n]}}),e.count=e.operation[e.operation.length-1].y1,NaN==e.count&&(e.count=0)}),console.log("Converted data after colours: ",o),f.domain(o.map(function(e){return e.bug_client_name})),h.domain([0,d3.max(o,function(e){return e.count})]),v.append("g").attr("class","x axis").attr("transform","translate(0,"+u+")").call(p),v.append("g").attr("class","y axis").call(_).append("text").attr("transform","rotate(-90)").attr("y",6).attr("dy",".71em").style("text-anchor","end").text("Count"),v.selectAll(".location").data(o).enter().append("g").attr("class","g").attr("transform",function(e){return"translate("+f(e.bug_client_name)+",0)"}).selectAll("rect").data(function(e){return e.operation}).enter().append("rect").attr("width",f.bandwidth()).attr("y",function(e){return h(e.y1)}).attr("height",function(e){return h(e.y0)-h(e.y1)}).attr("data-value",function(e){return e.y1-e.y0}).style("fill",function(e){return m(e.name)});var y=v.selectAll(".legend").data(m.domain().slice().reverse()).enter().append("g").attr("class","legend").attr("transform",function(e,t){return"translate(0,"+20*t+")"});y.append("rect").attr("x",d+48).attr("width",18).attr("height",18).style("fill",m),y.append("text").attr("x",d+48).attr("y",9).attr("dy",".35em").style("text-anchor","end").text(function(e){return e}),v.append("text").attr("x",d/2).attr("y",0-s/2).attr("text-anchor","middle").style("font-size","16px").style("text-decoration","underline").text("Bug Client Breakdown"),v.append("text").attr("transform","translate("+d/2+" ,"+(u+s+20)+")").style("text-anchor","middle").text("Bug Client Name"),v.append("text").attr("transform","rotate(-90)").attr("y",0-c).attr("x",0-u/2).attr("dy","1em").style("text-anchor","middle").text("Count of Bugs")}