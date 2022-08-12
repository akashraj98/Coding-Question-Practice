<h2><a href="https://leetcode.com/problems/next-greater-element-ii/">503. Next Greater Element II</a></h2><h3>Medium</h3><hr><div usedbyfluent="true"><p usedbyfluent="true">Given a circular integer array <code>nums</code> (i.e., the next element of <code>nums[nums.length - 1]</code> is <code>nums[0]</code>), return <em usedbyfluent="true">the <strong usedbyfluent="true">next greater number</strong> for every element in</em> <code>nums</code>.</p>

<p usedbyfluent="true">The <strong usedbyfluent="true">next greater number</strong> of a number <code>x</code> is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return <code>-1</code> for this number.</p>

<p usedbyfluent="true">&nbsp;</p>
<p><strong usedbyfluent="true">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
</pre>

<p><strong usedbyfluent="true">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4,3]
<strong>Output:</strong> [2,3,4,-1,4]
</pre>

<p usedbyfluent="true">&nbsp;</p>
<p><strong usedbyfluent="true">Constraints:</strong></p>

<ul usedbyfluent="true">
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>