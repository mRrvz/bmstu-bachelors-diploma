
struct page {
	unsigned long flags;
	union {
		struct {
			struct list_head lru;
			struct address_space *mapping;
			pgoff_t index;
			unsigned long private;
		};
	};

	union {
		atomic_t _mapcount;
		unsigned int page_type;
		unsigned int active;
		int units;
	};

	atomic_t _refcount;

#if defined(WANT_PAGE_VIRTUAL)
	void *virtual;
#endif
    int _last_cpupid;
} _struct_page_alignment;
