import json


def update_feed(json_feed_path, json_feed):
    with open(json_feed_path, 'r', encoding='utf8') as json_file:
        current = json.load(json_file)

    current_item_ids = [item['id'] for item in current.get('items', [])]

    for item in json_feed.get('items', []):
        if item['id'] not in current_item_ids:
            current['items'].append(item)

    json_feed['items'] = sorted(current.get('items', []),
                                key=lambda item: item.get('date_published', ''),
                                reverse=True)[:30]

    with open(json_feed_path, 'w', encoding='utf8') as json_file:
        json.dump(json_feed, json_file)
