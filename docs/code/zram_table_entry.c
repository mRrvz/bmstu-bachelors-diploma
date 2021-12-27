struct zram_table_entry {
	union {
		unsigned long handle;
		unsigned long element;
	};
	unsigned long flags;
#ifdef CONFIG_ZRAM_MEMORY_TRACKING
	ktime_t ac_time;
#endif