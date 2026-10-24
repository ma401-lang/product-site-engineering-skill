/**
 * Vendor-neutral observability adapters.
 *
 * Keep event fields explicit. Do not add request bodies, form values, chat text,
 * cookies, tokens, raw errors, email addresses, IP addresses, prompts, or model
 * output to these types.
 */

export type Outcome =
  | "success"
  | "rejected"
  | "timeout"
  | "cancelled"
  | "error";

export type BackendLogEvent = {
  timestamp: string;
  level: "debug" | "info" | "warn" | "error";
  event_name: string;
  service: string;
  environment: "local" | "test" | "preview" | "staging" | "production";
  release: string;
  request_id: string;
  outcome: Outcome;
  trace_id?: string;
  route?: string;
  method?: "GET" | "POST" | "PUT" | "PATCH" | "DELETE" | "HEAD" | "OPTIONS";
  status_code?: number;
  duration_ms?: number;
  error_code?: string;
  dependency?: string;
  retry_count?: number;
  time_to_first_chunk_ms?: number;
};

export type FrontendEvent = {
  timestamp: string;
  event_name: string;
  release: string;
  route: string;
  outcome: Outcome;
  request_id?: string;
  duration_bucket?:
    | "under_100ms"
    | "100_500ms"
    | "500ms_2s"
    | "2s_8s"
    | "8s_plus";
  client_error_code?: string;
};

type ServerSink = (serializedEvent: string) => void;
type BrowserSink = (event: FrontendEvent) => void | Promise<void>;

export function emitServerEvent(
  event: BackendLogEvent,
  sink: ServerSink,
): void {
  sink(JSON.stringify(event));
}

export async function emitBrowserEvent(
  event: FrontendEvent,
  sink: BrowserSink,
): Promise<void> {
  await sink(event);
}

export function durationBucket(durationMs: number): FrontendEvent["duration_bucket"] {
  if (durationMs < 100) return "under_100ms";
  if (durationMs < 500) return "100_500ms";
  if (durationMs < 2_000) return "500ms_2s";
  if (durationMs < 8_000) return "2s_8s";
  return "8s_plus";
}
