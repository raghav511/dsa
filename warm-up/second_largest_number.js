const arr = [2,5,1,-1,-1,3,0,10,6,-2,13,13,-3]
// arr=[-1,0]



const second_largest=(array)=>{
    let largest=Number.NEGATIVE_INFINITY
    let second_largest=largest-1
    for(element of array){
        if(element>largest && element!=largest){
            temp = largest
            largest=element
            second_largest=temp
        }
    }
    return(`${largest},${second_largest}`)
}

console.log(second_largest(arr))