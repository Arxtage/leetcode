<h2>62. Unique Paths</h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A robot is located at the top-left corner of a <code style="user-select: auto;">m x n</code> grid (marked 'Start' in the diagram below).</p>

<p style="user-select: auto;">The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).</p>

<p style="user-select: auto;">How many possible unique paths are there?</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" style="width: 400px; height: 183px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> m = 3, n = 7
<strong style="user-select: auto;">Output:</strong> 28
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> m = 3, n = 2
<strong style="user-select: auto;">Output:</strong> 3
<strong style="user-select: auto;">Explanation:</strong>
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right
3. Down -&gt; Right -&gt; Down
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> m = 7, n = 3
<strong style="user-select: auto;">Output:</strong> 28
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 4:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> m = 3, n = 3
<strong style="user-select: auto;">Output:</strong> 6
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= m, n &lt;= 100</code></li>
	<li style="user-select: auto;">It's guaranteed that the answer will be less than or equal to <code style="user-select: auto;">2 * 10<sup style="user-select: auto;">9</sup></code>.</li>
</ul>
</div>