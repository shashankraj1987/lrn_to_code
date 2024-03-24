let ARR=[1,3,5,7,9,11,13,17];

function binary_search(arr,start,end,elem){
	let mid=Math.floor((start+end)/2);
	console.log(" ");
	console.log(["Mid index is "+mid]);
	console.log(["Mid Element is " + arr[mid]]);
	let l_arr = arr.length;
	
	// This is the exit condition if element is not found
	if(start>end) return false;

	// If mid position value = element, then we found our value 
	if(arr[mid] === elem) return true;

	// If Mid is lesser than the elem, then our value is in the right
	
	if (arr[mid]<elem){
		return binary_search(arr,mid+1,l_arr-1,elem);
	}else if(arr[mid] > elem){
		return binary_search(arr,start,mid-1,elem);
	}
}

rand_num = Math.floor(Math.random()*ARR.length);
console.log(["Array is "+ARR]);
console.log(["Looking for "+rand_num]);
console.log(binary_search(ARR,0,ARR.length,rand_num));
