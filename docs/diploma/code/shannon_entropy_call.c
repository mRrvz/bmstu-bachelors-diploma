static int __zram_bvec_write(struct zram *zram, 
    struct bio_vec *bvec,
    u32 index, 
    struct bio *bio) {
...
    zstrm = zcomp_stream_get(zram->comp);
	src = kmap_atomic(page);

#ifdef CONFIG_ZRAM_ENTROPY
    entropy = shannon_entropy((const u8 *)src);
	if (entropy > CONFIG_ZRAM_ENTROPY_THRESHOLD)
		comp_len = PAGE_SIZE;
	else
		ret = zcomp_compress(zstrm, src, &comp_len);
#else
	ret = zcomp_compress(zstrm, src, &comp_len);
#endif

	kunmap_atomic(src);
...
}
