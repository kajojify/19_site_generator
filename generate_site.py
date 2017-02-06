import os
import copy
import os.path as op
import json
import markdown
from jinja2 import Environment, FileSystemLoader


def load_json(json_path):
    with open(json_path) as f:
        return json.load(f)


def set_environment(template_dir):
    template_env = Environment(loader=FileSystemLoader(template_dir))
    return template_env


def get_changed_articles(articles_config):
    articles = copy.deepcopy(articles_config)
    for article in articles:
        article_source = article['source']
        new_article_source = "{}.{}".format(op.splitext(article_source)[0],
                                            "html")
        article['source'] = new_article_source
    return articles


def render_templates(environment, conf_data, articles_dir):
    template = environment.get_template("base_index.html")
    articles_with_new_sources = get_changed_articles(conf_data['articles'])
    index_rendered = template.render(all_topics=conf_data['topics'],
                                     all_articles=articles_with_new_sources)
    index_path = "index.html"
    yield (index_path, index_rendered)
    template = environment.get_template("base_article.html")
    for article in conf_data['articles']:
        full_article_source = op.join(articles_dir, article['source'])
        with open(full_article_source) as f:
            article_html = markdown.markdown(f.read())
        rendered_template = template.render(title=article['title'],
                                            content=article_html)
        yield (article['source'], rendered_template)


def create_dirs(full_path):
    html_dir = op.dirname(full_path)
    if not op.exists(html_dir):
        os.makedirs(html_dir)


def create_html_page(html_path, template):
    new_html_path = "{}.{}".format(op.splitext(html_path)[0], "html")
    with open(new_html_path, "w") as html:
        html.write(template)


if __name__ == '__main__':
    articles_dir = "articles"
    template_dir = "templates"
    config_path = "config.json"
    conf_data = load_json(config_path)
    site_dir = input("Enter the path to the site folder:  ---  ")
    if not op.isdir(site_dir):
        os.mkdir(site_dir)
    template_env = set_environment(template_dir)
    for path, html in render_templates(template_env, conf_data, articles_dir):
        full_path = op.join(site_dir, path)
        create_dirs(full_path)
        create_html_page(full_path, html)
