<h2>452. Minimum Number of Arrows to Burst Balloons</h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.</p>

<p style="user-select: auto;">An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with <code style="user-select: auto;">x<sub style="user-select: auto;">start</sub></code> and <code style="user-select: auto;">x<sub style="user-select: auto;">end</sub></code> bursts by an arrow shot at <code style="user-select: auto;">x</code> if <code style="user-select: auto;">x<sub style="user-select: auto;">start</sub> ≤ x ≤ x<sub style="user-select: auto;">end</sub></code>. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.</p>

<p style="user-select: auto;">Given an array <code style="user-select: auto;">points</code> where <code style="user-select: auto;">points[i] = [x<sub style="user-select: auto;">start</sub>, x<sub style="user-select: auto;">end</sub>]</code>, return <em style="user-select: auto;">the minimum number of arrows that must be shot to burst all balloons</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> points = [[10,16],[2,8],[1,6],[7,12]]
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explanation:</strong> One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> points = [[1,2],[3,4],[5,6],[7,8]]
<strong style="user-select: auto;">Output:</strong> 4
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> points = [[1,2],[2,3],[3,4],[4,5]]
<strong style="user-select: auto;">Output:</strong> 2
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= points.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">points[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-2<sup style="user-select: auto;">31</sup> &lt;= x<sub style="user-select: auto;">start</sub> &lt; x<sub style="user-select: auto;">end</sub> &lt;= 2<sup style="user-select: auto;">31</sup> - 1</code></li>
</ul>
</div>