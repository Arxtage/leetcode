<h2>57. Insert Interval</h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a set of <em style="user-select: auto;">non-overlapping</em> intervals, insert a new interval into the intervals (merge if necessary).</p>

<p style="user-select: auto;">You may assume that the intervals were initially sorted according to their start times.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> intervals = [[1,3],[6,9]], newInterval = [2,5]
<strong style="user-select: auto;">Output:</strong> [[1,5],[6,9]]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
<strong style="user-select: auto;">Output:</strong> [[1,2],[3,10],[12,16]]
<strong style="user-select: auto;">Explanation:</strong> Because the new interval <code style="user-select: auto;">[4,8]</code> overlaps with <code style="user-select: auto;">[3,5],[6,7],[8,10]</code>.</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> intervals = [], newInterval = [5,7]
<strong style="user-select: auto;">Output:</strong> [[5,7]]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 4:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> intervals = [[1,5]], newInterval = [2,3]
<strong style="user-select: auto;">Output:</strong> [[1,5]]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 5:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> intervals = [[1,5]], newInterval = [2,7]
<strong style="user-select: auto;">Output:</strong> [[1,7]]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= intervals.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">intervals[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;=&nbsp;intervals[i][0] &lt;=&nbsp;intervals[i][1] &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">intervals</code>&nbsp;is sorted by <code style="user-select: auto;">intervals[i][0]</code> in <strong style="user-select: auto;">ascending</strong>&nbsp;order.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">newInterval.length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;=&nbsp;newInterval[0] &lt;=&nbsp;newInterval[1] &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
</ul>
</div>