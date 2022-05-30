struct zram {
	struct zram_table_entry *table;
	struct zs_pool *mem_pool;
	struct zcomp *comp;
	struct gendisk *disk;
	struct rw_semaphore init_lock;
	unsigned long limit_pages;

	struct zram_stats stats;
	u64 disksize;
	char compressor[CRYPTO_MAX_ALG_NAME];
	bool claim;
#ifdef CONFIG_ZRAM_WRITEBACK
	struct file *backing_dev;
	spinlock_t wb_limit_lock;
	bool wb_limit_enable;
	u64 bd_wb_limit;
	struct block_device *bdev;
	unsigned long *bitmap;
	unsigned long nr_pages;
#endif
#ifdef CONFIG_ZRAM_MEMORY_TRACKING
	struct dentry *debugfs_dir;
#endif
};