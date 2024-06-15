---
distance: 12
someComputedValue: 14
someInputValue: 7
count: "0"
---
### Hello
```python
def doSomething(n: int):
	print('Hello ')
```

Distance: `INPUT[number:distance]` km
Distance in freedom units: `VIEW[{distance}]` miles

Input: `INPUT[number:someInputValue]`
Computed Value: `VIEW[{someInputValue} * 2][math:someComputedValue]`

```meta-bind-button
label: "+1"
hidden: true
id: "count-increment"
style: default
actions:
  - type: updateMetadata
    bindTarget: count
    evaluate: true
    value: x + 1
```

```meta-bind-button
label: "-1"
hidden: true
id: "count-decrement"
style: default
actions:
  - type: updateMetadata
    bindTarget: count
    evaluate: true
    value: x - 1
```

```meta-bind-button
label: "Reset"
hidden: true
id: "count-reset"
style: default
actions:
  - type: updateMetadata
    bindTarget: count
    evaluate: false
    value: 0
```

`BUTTON[count-decrement, count-reset, count-increment]` `VIEW[{count}]`
