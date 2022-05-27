static inline u32 ilog2_w(u64 n)
{
	return ilog2(n * n * n * n);
}

static inline s32 shannon_entropy(const u8 *src)
{
	s32 entropy_sum = 0;
	u32 sz_base, i;
	u16 entropy_count[256] = { 0 };

	for (i = 0; i < PAGE_SIZE; ++i)
		entropy_count[src[i]]++;

	sz_base = ilog2_w(PAGE_SIZE);
	for (i = 0; i < ARRAY_SIZE(entropy_count); ++i) {
		if (entropy_count[i] > 0) {
			s32 p = entropy_count[i];

			entropy_sum += p * (sz_base - ilog2_w((u64)p));
		}
	}

	return entropy_sum;
}
