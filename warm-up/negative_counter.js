arr = [2,5,1,-1,-1,3,0,10,6,-2,11,13,-3]
const negative_numbers = (array)=>{
    let negative_counter = 0
    for(element of array){
        if(element<0){
            negative_counter=negative_counter+1
        }
    }
    return negative_counter
}

console.log(negative_numbers(arr))