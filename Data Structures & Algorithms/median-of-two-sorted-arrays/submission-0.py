class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2

        # Search the shorter array.
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        left_size = (total + 1) // 2
        lo, hi = 0, len(A)

        while lo <= hi:
            i = (lo + hi) // 2
            j = left_size - i

            a_left = A[i - 1] if i > 0 else float("-inf")
            a_right = A[i] if i < len(A) else float("inf")
            b_left = B[j - 1] if j > 0 else float("-inf")
            b_right = B[j] if j < len(B) else float("inf")

            if a_left > b_right:
                hi = i - 1
            elif b_left > a_right:
                lo = i + 1
            else:
                if total % 2:
                    return float(max(a_left, b_left))

                return (
                    max(a_left, b_left) + min(a_right, b_right)
                ) / 2