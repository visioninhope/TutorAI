""" This is the post-processing module for the text scraper. It contains a class that performs post-processing on the extracted text data. The post-processing class is responsible for cleaning up the extracted text data and extracting paragraphs from the page content. The extracted paragraphs are then stored in a data class object for further processing."""

from dataclasses import dataclass


@dataclass
class Page:
    text: str
    page_num: int
    pdf_name: str


class PostProcessor:

    def page_post_processing(self, pages: list[Page]) -> list[Page]:
        post_processed_pages = []

        for page in pages:
            post_processed_pages.append(self._extract_paragraphs(page))

        return post_processed_pages

    def _extract_paragraphs(self, page: Page) -> Page:
        """
        Extract paragraphs from a list of strings, where each string represents page content from a PDF.

        Parameters:
        - page_data: list of strings, where each string represents the content of a page.

        Returns:
        - A list of paragraphs extracted from the page content.
        """

        # Split the page into segments based on double newline characters
        # segments = page.split("\n\n")

        # Further process each segment
        # for segment in segments:
        #     # Clean up the segment by stripping leading/trailing whitespace and replacing multiple newlines with a single space
        #     cleaned_segment = ' '.join(segment.strip().split('\n'))
        #     cleaned_segment = self.simple_clean(cleaned_segment)

        #     # Ignore empty segments
        cleaned_segment = self._simple_clean(page.text)
        page.text = cleaned_segment

        return page

    def _simple_clean(self, text, replace_with="?"):

        return "".join(char if ord(char) < 255 else replace_with for char in text)
