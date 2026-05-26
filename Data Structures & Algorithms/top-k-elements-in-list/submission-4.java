class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Map Initialization
        Map<Integer, Integer> freqMap = new HashMap<>();

        // Get or default syntax
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // An array[] of Lists syntax
        List<Integer>[] buckets = IntStream.range(0, nums.length + 1)
            .mapToObj(i -> new ArrayList<Integer>())
            .toArray(List[]::new);

        for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
            int freq = entry.getValue();
            int num = entry.getKey();
            buckets[freq].add(num);
        }

        List<Integer> result = new ArrayList<>();
        for (int i = buckets.length - 1; i >= 0 && result.size() < k; i--) {
            if (!buckets[i].isEmpty()) {
                result.addAll(buckets[i]);
            }
        }

        return result.stream().mapToInt(i -> i).toArray();
    }
}
