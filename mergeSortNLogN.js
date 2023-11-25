function mergeSort(arr){
    if(arr.length < 2) {
        return arr;
    }

    const midIndex = Math.floor(arr.length / 2);
    const leftArr = arr.slice(0, midIndex);
    const rightArr = arr.slice(midIndex, arr.length);

    return merge(mergeSort(leftArr), mergeSort(rightArr));
}

function merge(leftArr, rightArr){
    let resultArr = [];
    let leftIndex= 0;
    let rightIndex = 0;

    while(leftIndex < leftArr.length && rightIndex < rightArr.length) {
        if(leftArr[leftIndex] < rightArr[rightIndex]){
            resultArr.push(leftArr[leftIndex]);
            leftIndex += 1;
        } else {
            resultArr.push(rightArr[rightIndex]);
            rightIndex += 1;
        }
    }
    return resultArr.concat(leftArr.slice(leftIndex)).concat(rightArr.slice(rightIndex));
}


arr = [5, 334, 53, 56, 23, 12]

console.log(mergeSort(arr));