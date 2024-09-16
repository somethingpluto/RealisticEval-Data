function convert_thread_to_JSON_file(thread)
{
    let data = thread;
    let string = JSON.stringify(data);
    let blob = encode_string_as_blob(string);
    return blob;
}