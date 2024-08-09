		bool CalculateOverlap(const float2& min1, const float2& max1, const float2& min2, const float2& max2, float2& out)
		{
			// General collison insight inspired by javidx9 on youtube.
			// https://www.youtube.com/watch?v=8JJ-4JgR7Dg
			// 
			// CalculateOverlap function written by ChatGPT and than modified.
			//

			out = { 0, 0 };

			// Calculate the overlap in every axis.
			const float overlapX = Math::Min(max1.x, max2.x) - Math::Max(min1.x, min2.x);
			const float overlapY = Math::Min(max1.y, max2.y) - Math::Max(min1.y, min2.y);

			// Determine the direction of overlap to find the collision normal
			if (overlapX < overlapY) {
				// Collision is primarily along the X-axis
				if (min1.x < min2.x)
					out.x = -overlapX;
				else
					out.x = overlapX;
			}
			else {
				// Collision is primarily along the Y-axis
				if (min1.y < min2.y) {
					out.y = -overlapY;
				}
				else {
					out.y = overlapY;
				}
			}

			return out.x != 0 || out.y != 0;
		}
