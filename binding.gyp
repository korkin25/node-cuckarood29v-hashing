{
    "targets": [
        {
            "target_name": "cuckarood29v-hashing",
            "sources": [
                "cuckarood29v.cc",
                "src/blake2b-ref.c"
            ],
            "include_dirs": [
                "src",
                "<!(node -e \"require('nan')\")"
            ]
        }
    ]
}
