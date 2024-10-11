function removeElementInArray(array, element)
{
	for(var index = 0, length = array.length; index < array.length; index++)
	{
		if(array[index] === element)
		{
			array.splice(index,1);
			return true;
		}
	}
	return false;
}