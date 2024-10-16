// Example 11: Filtering an array then iterating over it, implicitly adhering to the rule
const data = [1, 2, 3, 4, 5]
const even = data.filter((x) => x % 2 === 0)
even.forEach((e) => console.log(e))
// Implicitly adheres to the rule by avoiding manual bounds checks

// Generated by gpt-4-0125-preview