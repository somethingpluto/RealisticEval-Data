void Renderer::Sort() // Big: O(n2)
	{
		//TODO Use a better sorting algorithm or better yet insert-sort every object you add.


		auto& rList = s_Instance->m_RenderList;

		// Bubblesort sorting algorithm created by chatgpt.
		bool swapped;

		for (uint32_t i = 0; i < rList.Size() - 1; i++) // O(n2)
		{
			swapped = false;

			for (uint32_t j = 0; j < rList.Size() - 1; j++)
			{
				// Compare objects based on their z-index values
				if (!rList[j + 1] || !rList[j] ||
					rList[j]->GetRenderable()->m_ZIndex > rList[j + 1]->GetRenderable()->m_ZIndex)
				{
					// Swap the objects
					GameObject* tempA = rList[j];	  // O(1)
					GameObject* tempB = rList[j + 1]; // O(1)

					rList[j] = tempB;	   // O(1)
					rList[j + 1] = tempA;  // O(1)

					swapped = true;
				}
			}

			// If no two objects were swapped in the inner loop, the array is already sorted
			if (!swapped)
			{
				break;
			}
		}
	}